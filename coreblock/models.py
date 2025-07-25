from django.db import models, transaction
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Sum, Q
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from decimal import Decimal
import datetime
from simple_history.models import HistoricalRecords

class BusinessLogicError(Exception):
    """Custom exception for business logic errors outside form validation."""
    pass

class ActiveManager(models.Manager):
    """Manager for retrieving only active (non-deleted) records."""
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, deleted_at__isnull=True)

class VatRateManager(models.Manager):
    def get_rate_for_date(self, date):
        """Get the VAT rate effective for a given date."""
        try:
            return self.filter(
                Q(effective_to__gte=date) | Q(effective_to__isnull=True),
                effective_from__lte=date
            ).order_by('-effective_from').first().rate
        except AttributeError:
            raise BusinessLogicError(f"No VAT rate defined for date {date}.")
        except self.model.MultipleObjectsReturned:
            raise BusinessLogicError(f"Multiple VAT rates defined for date {date}.")

class VatRate(models.Model):
    rate = models.DecimalField(max_digits=5, decimal_places=4)  # e.g., 0.1500 for 15%
    effective_from = models.DateField()
    effective_to = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    objects = VatRateManager()
    active_objects = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        db_table = 'vat_rate'
        indexes = [
            models.Index(fields=['effective_from', 'effective_to']),
        ]

    def __str__(self):
        return f"{self.rate*100}% ({self.effective_from} to {self.effective_to or 'ongoing'})"

    def clean(self):
        if self.effective_to and self.effective_from > self.effective_to:
            raise ValidationError({'effective_to': "Effective end date must be after start date."})
        # Check for overlapping periods
        overlapping = VatRate.objects.filter(
            effective_from__lte=self.effective_to if self.effective_to else datetime.date(9999, 12, 31)
        ).filter(
            Q(effective_to__gte=self.effective_from) | Q(effective_to__isnull=True)
        ).exclude(pk=self.pk)
        if overlapping.exists():
            raise ValidationError("VAT rate period overlaps with an existing rate.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class SystemAccount(models.Model):
    type = models.CharField(max_length=50, unique=True, choices=[
        ('LIABILITY_PAYMENTS', 'Liability Payments'),
        ('ASSET_RECEIVABLES', 'Asset Receivables'),
        ('VAT_LIABILITY', 'VAT Liability'),
        ('TRUST_ACCOUNT', 'Trust Account'),
    ])
    account = models.ForeignKey('ChartOfAccount', on_delete=models.CASCADE, related_name='system_accounts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    history = HistoricalRecords()

    objects = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        db_table = 'system_account'

    def __str__(self):
        return f"{self.type} -> {self.account.name}"

class ChartOfAccountManager(models.Manager):
    def create_account(self, code, name, account_type):
        """Create a chart of account with validation."""
        if not code or not name:
            raise ValidationError("Account code and name are required.")
        account = self.model(code=code, name=name, account_type=account_type)
        account.full_clean()
        account.save()
        return account

class ChartOfAccount(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
        ('ASSET', 'Asset'),
        ('LIABILITY', 'Liability'),
        ('TRUST', 'Trust Account')
    ]
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    account_type = models.CharField(max_length=50, choices=ACCOUNT_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    objects = ChartOfAccountManager()
    active_objects = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        db_table = 'chart_of_account'
        indexes = [
            models.Index(fields=['code', 'account_type']),
        ]

    def __str__(self):
        return f"{self.code} - {self.name} ({self.account_type})"

    def clean(self):
        if self.account_type not in dict(self.ACCOUNT_TYPE_CHOICES).keys():
            raise ValidationError({'account_type': "Invalid account type."})

class ClientManager(models.Manager):
    def create_client(self, name, email=None, identity_number=None, registration_number=None, trust_date=None, trust_division=None, is_trust=False, marital_status=None, user=None):
        """Create a client with validation, supporting trust accounts."""
        if not name:
            raise ValidationError("Client name is required.")
        if identity_number and self.filter(identity_number=identity_number).exists():
            raise ValidationError("Identity number must be unique.")
        if is_trust and not registration_number:
            raise ValidationError("Registration number is required for trust clients.")
        client = self.create(
            name=name,
            email=email,
            identity_number=identity_number,
            registration_number=registration_number,
            trust_date=trust_date,
            trust_division=trust_division,
            is_trust=is_trust,
            marital_status=marital_status,
            user=user,
            income_ytd=Decimal('0.00'),
            expense_ytd=Decimal('0.00'),
            trust_balance=Decimal('0.00')
        )
        return client

    def get_year_end_report(self, client_id, year):
        """Generate year-end financial report for a client, including trust transactions and VAT."""
        client = self.get(pk=client_id)
        transactions = FinancialTransaction.history.filter(
            matter__client=client,
            matter__is_active=True,
            transaction_date__year=year,
            is_active=True
        )
        total_income = transactions.filter(transaction_type='INCOME').aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')
        total_expense = transactions.filter(transaction_type='EXPENSE').aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')
        total_trust = transactions.filter(transaction_type__in=['TRUST_DEPOSIT', 'TRUST_DISBURSEMENT']).aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')
        total_vat = transactions.filter(transaction_type='VAT').aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')
        return {
            'client': client.name,
            'year': year,
            'income_ytd': client.income_ytd or Decimal('0.00'),
            'expense_ytd': client.expense_ytd or Decimal('0.00'),
            'trust_balance': client.trust_balance or Decimal('0.00'),
            'transaction_income': total_income,
            'transaction_expense': total_expense,
            'transaction_trust': total_trust,
            'total_vat': total_vat
        }

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    identity_number = models.CharField(max_length=255, null=True, blank=True, unique=True)
    registration_number = models.CharField(max_length=255, null=True, blank=True)
    trust_date = models.DateField(null=True, blank=True)
    trust_division = models.CharField(max_length=255, null=True, blank=True)
    is_trust = models.BooleanField(default=False)
    marital_status = models.CharField(max_length=1, choices=[('S', 'Single'), ('M', 'Married'), ('D', 'Divorced')], null=True, blank=True)
    income_ytd = models.DecimalField(max_digits=19, decimal_places=4, null=True, blank=True)
    expense_ytd = models.DecimalField(max_digits=19, decimal_places=4, null=True, blank=True)
    trust_balance = models.DecimalField(max_digits=19, decimal_places=4, default=Decimal('0.00'))
    vat_number = models.CharField(max_length=255, null=True, blank=True)
    physical_address = models.CharField(max_length=255, null=True, blank=True)
    postal_address = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    objects = ClientManager()
    active_objects = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        db_table = 'client'
        indexes = [
            models.Index(fields=['name', 'email']),
            models.Index(fields=['identity_number']),
            models.Index(fields=['is_trust']),
        ]
        permissions = [
            ("view_client", "Can view client"),
            ("manage_client", "Can manage client"),
        ]

    def __str__(self):
        return self.name

    def clean(self):
        if self.trust_balance < 0:
            raise ValidationError({'trust_balance': "Trust balance cannot be negative."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class EmployeeManager(models.Manager):
    def create_employee(self, name, email, user=None):
        """Create an employee with validation."""
        if not name or not email:
            raise ValidationError("Name and email are required.")
        if self.filter(email=email).exists():
            raise ValidationError("Email must be unique.")
        employee = self.create(name=name, email=email, user=user)
        return employee

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    objects = EmployeeManager()
    active_objects = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        db_table = 'employee'
        indexes = [
            models.Index(fields=['name', 'email']),
        ]
        permissions = [
            ("view_employee", "Can view employee"),
            ("manage_employee", "Can manage employee"),
        ]

    def __str__(self):
        return self.name

class CreditorManager(models.Manager):
    def create_creditor(self, name, amount_owed, client=None, external_ref=None):
        """Create a creditor with validation."""
        if not name or amount_owed < 0:
            raise ValidationError("Creditor name and non-negative amount owed are required.")
        creditor = self.create(name=name, amount_owed=amount_owed, client=client, external_ref=external_ref)
        return creditor

class Creditor(models.Model):
    name = models.CharField(max_length=255)
    amount_owed = models.DecimalField(max_digits=19, decimal_places=4)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name='creditors')
    external_ref = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    objects = CreditorManager()
    active_objects = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        db_table = 'creditor'
        indexes = [
            models.Index(fields=['name', 'client']),
        ]
        permissions = [
            ("view_creditor", "Can view creditor"),
            ("manage_creditor", "Can manage creditor"),
        ]

    def __str__(self):
        return f"{self.name} ({self.amount_owed})"

    @transaction.atomic
    def record_payment(self, amount, matter, recorded_by, transaction_date, account=None):
        """Record a payment to the creditor."""
        if amount <= 0:
            raise ValidationError("Payment amount must be positive.")
        if amount > self.amount_owed:
            raise ValidationError("Payment cannot exceed amount owed.")
        try:
            account = account or SystemAccount.active_objects.get(type='LIABILITY_PAYMENTS').account
        except SystemAccount.DoesNotExist:
            raise BusinessLogicError("Liability payments account not configured.")
        FinancialTransaction.objects.create_transaction(
            matter=matter,
            description=f"Payment to creditor {self.name}",
            amount=amount,
            transaction_type='EXPENSE',
            transaction_date=transaction_date,
            recorded_by=recorded_by,
            vat_flag=False,
            account=account,
            is_trust_transaction=False
        )
        self.amount_owed -= amount
        self.full_clean()
        self.save()

class DebtorManager(models.Manager):
    def create_debtor(self, name, amount_due, client=None, external_ref=None):
        """Create a debtor with validation."""
        if not name or amount_due < 0:
            raise ValidationError("Debtor name and non-negative amount due are required.")
        debtor = self.create(name=name, amount_due=amount_due, client=client, external_ref=external_ref)
        return debtor

class Debtor(models.Model):
    name = models.CharField(max_length=255)
    amount_due = models.DecimalField(max_digits=19, decimal_places=4)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name='debtors')
    external_ref = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    objects = DebtorManager()
    active_objects = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        db_table = 'debtor'
        indexes = [
            models.Index(fields=['name', 'client']),
        ]
        permissions = [
            ("view_debtor", "Can view debtor"),
            ("manage_debtor", "Can manage debtor"),
        ]

    def __str__(self):
        return f"{self.name} ({self.amount_due})"

    @transaction.atomic
    def record_receipt(self, amount, matter, recorded_by, transaction_date, account=None):
        """Record a receipt from the debtor."""
        if amount <= 0:
            raise ValidationError("Receipt amount must be positive.")
        if amount > self.amount_due:
            raise ValidationError("Receipt cannot exceed amount due.")
        try:
            account = account or SystemAccount.active_objects.get(type='ASSET_RECEIVABLES').account
        except SystemAccount.DoesNotExist:
            raise BusinessLogicError("Asset receivables account not configured.")
        FinancialTransaction.objects.create_transaction(
            matter=matter,
            description=f"Receipt from debtor {self.name}",
            amount=amount,
            transaction_type='INCOME',
            transaction_date=transaction_date,
            recorded_by=recorded_by,
            vat_flag=False,
            account=account,
            is_trust_transaction=False
        )
        self.amount_due -= amount
        self.full_clean()
        self.save()

class MatterManager(models.Manager):
    def create_matter(self, client, description, matter_type, created_by):
        """Create a matter with validation."""
        if matter_type not in dict(Matter.MATTER_TYPE_CHOICES).keys():
            raise ValidationError("Invalid matter type.")
        matter = self.create(
            client=client,
            description=description,
            matter_type=matter_type,
            created_by=created_by
        )
        return matter

class Matter(models.Model):
    MATTER_TYPE_CHOICES = [
        ('BOND', 'Bond Registration'),
        ('TRUST', 'Trust Transaction'),
        ('TRANSFER', 'Property Transfer'),
        ('OTHER', 'Other')
    ]
    STATUS_CHOICES = [
        ('INSTRUCTED', 'Instructed'),
        ('LODGED', 'Lodged'),
        ('REGISTERED', 'Registered'),
        ('COMPLETED', 'Completed')
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='matters')
    description = models.CharField(max_length=255)
    matter_type = models.CharField(max_length=50, choices=MATTER_TYPE_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='INSTRUCTED')
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='created_matters')
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    objects = MatterManager()
    active_objects = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        db_table = 'matter'
        indexes = [
            models.Index(fields=['client', 'matter_type']),
            models.Index(fields=['status']),
        ]
        permissions = [
            ("view_matter", "Can view matter"),
            ("manage_matter", "Can manage matter"),
        ]

    def __str__(self):
        return f"{self.description} ({self.client.name})"

class FinancialTransactionManager(models.Manager):
    def create_transaction(self, matter, description, amount, transaction_type, transaction_date, recorded_by, vat_flag=False, account=None, is_trust_transaction=False):
        """Create a financial transaction with validation."""
        if amount < 0:
            raise ValidationError("Amount cannot be negative.")
        if transaction_type not in dict(FinancialTransaction.TRANSACTION_TYPE_CHOICES).keys():
            raise ValidationError("Invalid transaction type.")
        if is_trust_transaction and not matter.client.is_trust:
            raise ValidationError("Trust transactions require a trust client.")
        if is_trust_transaction and not account.account_type == 'TRUST':
            raise ValidationError("Trust transactions require a trust account.")
        with transaction.atomic():
            transaction = self.create(
                matter=matter,
                description=description,
                amount=amount,
                transaction_type=transaction_type,
                transaction_date=transaction_date,
                recorded_by=recorded_by,
                vat_flag=vat_flag,
                account=account,
                is_trust_transaction=is_trust_transaction
            )
            if vat_flag:
                transaction.calculate_vat()
        return transaction

class FinancialTransaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('FEE', 'Attorney Fee'),
        ('TRANSFER_DUTY', 'Transfer Duty'),
        ('BOND_AMOUNT', 'Bond Amount'),
        ('VAT', 'VAT'),
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
        ('TRUST_DEPOSIT', 'Trust Deposit'),
        ('TRUST_DISBURSEMENT', 'Trust Disbursement'),
        ('OTHER', 'Other')
    ]
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE, related_name='transactions')
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=19, decimal_places=4)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPE_CHOICES)
    transaction_date = models.DateField()
    vat_flag = models.BooleanField(default=False)
    recorded_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='recorded_transactions')
    account = models.ForeignKey(ChartOfAccount, on_delete=models.SET_NULL, null=True, related_name='transactions')
    is_trust_transaction = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    objects = FinancialTransactionManager()
    active_objects = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        db_table = 'financial_transaction'
        indexes = [
            models.Index(fields=['matter', 'transaction_date']),
            models.Index(fields=['transaction_type', 'is_trust_transaction']),
            models.Index(fields=['account']),
        ]
        permissions = [
            ("view_financial_transaction", "Can view financial transaction"),
            ("manage_financial_transaction", "Can manage financial transaction"),
        ]

    def __str__(self):
        return f"{self.description} ({self.amount})"

    @transaction.atomic
    def calculate_vat(self):
        """Calculate and create a VAT transaction if vat_flag is True."""
        if self.vat_flag and self.transaction_type != 'VAT':
            try:
                system_account = SystemAccount.active_objects.get(type='VAT_LIABILITY')
                vat_rate = VatRate.objects.get_rate_for_date(self.transaction_date)
                vat_amount = self.amount * vat_rate
                FinancialTransaction.objects.create(
                    matter=self.matter,
                    description=f"VAT for {self.description}",
                    amount=vat_amount,
                    transaction_type='VAT',
                    transaction_date=self.transaction_date,
                    recorded_by=self.recorded_by,
                    vat_flag=False,
                    account=system_account.account,
                    is_trust_transaction=False
                )
            except SystemAccount.DoesNotExist:
                raise BusinessLogicError("VAT liability account not configured.")
            except BusinessLogicError as e:
                raise BusinessLogicError(f"VAT calculation failed: {str(e)}")

@receiver(post_save, sender=FinancialTransaction)
@receiver(post_delete, sender=FinancialTransaction)
def update_client_balances(sender, instance, **kwargs):
    """Update client balances on transaction save or delete."""
    with transaction.atomic():
        client = Client.objects.select_for_update().get(pk=instance.matter.client.pk)
        year = instance.transaction_date.year
        transactions = FinancialTransaction.active_objects.filter(
            matter__client=client,
            matter__is_active=True,
            transaction_date__year=year,
            is_active=True
        )
        client.income_ytd = transactions.filter(transaction_type='INCOME').aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')
        client.expense_ytd = transactions.filter(transaction_type='EXPENSE').aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')
        trust_deposits = transactions.filter(transaction_type='TRUST_DEPOSIT').aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')
        trust_disbursements = transactions.filter(transaction_type='TRUST_DISBURSEMENT').aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')
        client.trust_balance = trust_deposits - trust_disbursements
        client.full_clean()
        client.save()
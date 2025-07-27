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
        vat_obj = self.filter(
            Q(effective_to__gte=date) | Q(effective_to__isnull=True),
            effective_from__lte=date
        ).order_by('-effective_from').first()
        if vat_obj is None:
            raise BusinessLogicError(f"No VAT rate defined for date {date}.")
        return vat_obj.rate

class VatRate(models.Model):
    rate = models.DecimalField(max_digits=5, decimal_places=4)  # e.g., 0.1500 for 15%
    effective_from = models.DateField()
    effective_to = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    objects = VatRateManager() # Custom manager for VAT rates
    all_objects = models.Manager() # Default manager for all objects

    def __str__(self):
        return f"{self.rate*100:.2f}% from {self.effective_from} to {self.effective_to or 'present'}"

    class Meta:
        unique_together = ('rate', 'effective_from')
        ordering = ['-effective_from']


class ChartOfAccountManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, deleted_at__isnull=True)

class ChartOfAccount(models.Model):
    ACCOUNT_TYPES = [
        ('ASSET', 'Asset'),
        ('LIABILITY', 'Liability'),
        ('EQUITY', 'Equity'),
        ('REVENUE', 'Revenue'),
        ('EXPENSE', 'Expense'),
        ('TRUST', 'Trust'),
    ]
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    objects = ChartOfAccountManager()
    all_objects = models.Manager()

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        ordering = ['code']


class SystemAccountManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, deleted_at__isnull=True)

class SystemAccount(models.Model):
    ACCOUNT_CHOICES = [
        ('LIABILITY_PAYMENTS', 'Liability Payments Account'),
        ('ASSET_RECEIVABLES', 'Asset Receivables Account'),
        ('VAT_LIABILITY', 'VAT Liability Account'),
        ('TRUST_ACCOUNT', 'Trust Account'),
    ]
    type = models.CharField(max_length=50, choices=ACCOUNT_CHOICES, unique=True)
    account = models.ForeignKey(ChartOfAccount, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    objects = SystemAccountManager()
    all_objects = models.Manager()

    def __str__(self):
        return f"System Account {self.type}: {self.account.name}"

    class Meta:
        ordering = ['type']


class ClientManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, deleted_at__isnull=True)

class Client(models.Model):
    PRACTICE_AREAS = [
        ('LITIGATION', 'Litigation'),
        ('CORPORATE', 'Corporate Law'),
        ('FAMILY', 'Family Law'),
        ('PROPERTY', 'Property Law'),
        ('CRIMINAL', 'Criminal Law'),
    ]
    name = models.CharField(max_length=255, unique=True)
    practice_area = models.CharField(max_length=100, choices=PRACTICE_AREAS)
    income_ytd = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    expense_ytd = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    trust_balance = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    objects = ClientManager()
    all_objects = models.Manager() # Default manager for all objects

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'practice_area')
        ordering = ['name']
        permissions = [
            ("view_client_detailed", "Can view detailed client information"),
            # Removed: ("view_client", "Can view client"),
        ]

class EmployeeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, deleted_at__isnull=True)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    objects = EmployeeManager()
    all_objects = models.Manager()

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['user__username']
        permissions = [
            # Removed: ("view_employee", "Can view employee"),
        ]


class CreditorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, deleted_at__isnull=True)

class Creditor(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField(blank=True, null=True)
    tax_id = models.CharField(max_length=50, blank=True, null=True)
    bank_account_details = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    objects = CreditorManager()
    all_objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        permissions = [
            # Removed: ("view_creditor", "Can view creditor"),
        ]


class DebtorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, deleted_at__isnull=True)

class Debtor(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField(blank=True, null=True)
    tax_id = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    objects = DebtorManager()
    all_objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        permissions = [
            # Removed: ("view_debtor", "Can view debtor"),
        ]

class MatterManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, deleted_at__isnull=True)

class Matter(models.Model):
    MATTER_TYPES = [
        ('LITIGATION', 'Litigation'),
        ('CORPORATE', 'Corporate Law'),
        ('FAMILY', 'Family Law'),
        ('PROPERTY', 'Property Law'),
        ('CRIMINAL', 'Criminal Law'),
        ('GENERAL', 'General Advisory'),
    ]
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
        ('PENDING', 'Pending'),
    ]
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='matters')
    matter_type = models.CharField(max_length=100, choices=MATTER_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='matters_created')
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    objects = MatterManager()
    all_objects = models.Manager()

    def __str__(self):
        return f"{self.description[:50]}... ({self.client.name})"

    class Meta:
        ordering = ['-created_at']
        permissions = [
            # Removed: ("view_matter", "Can view matter"),
        ]

class FinancialTransactionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, deleted_at__isnull=True)

    def calculate_total_for_matter(self, matter_id):
        """Calculate total amount for a given matter."""
        return self.filter(matter__id=matter_id).aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')

    def calculate_total_for_client(self, client_id, transaction_type=None):
        """Calculate total amount for a given client, optionally filtered by type."""
        qs = self.filter(matter__client__id=client_id)
        if transaction_type:
            qs = qs.filter(transaction_type=transaction_type)
        return qs.aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')


class FinancialTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
        ('TRUST_DEPOSIT', 'Trust Deposit'),
        ('TRUST_DISBURSEMENT', 'Trust Disbursement'),
    ]
    description = models.TextField()
    matter = models.ForeignKey(Matter, on_delete=models.PROTECT, related_name='financial_transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    transaction_date = models.DateField()
    recorded_by = models.ForeignKey(User, on_delete=models.PROTECT)
    vat_flag = models.BooleanField(default=False)
    vat_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    account = models.ForeignKey(ChartOfAccount, on_delete=models.PROTECT, related_name='transactions')
    is_trust_transaction = models.BooleanField(default=False) # True if transaction involves trust account
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    objects = FinancialTransactionManager()
    active_objects = ActiveManager() # Manager for active transactions only
    all_objects = models.Manager()

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} for {self.matter.description[:30]}..."

    def clean(self):
        if self.vat_flag and self.vat_amount is None:
            raise ValidationError("VAT amount is required if VAT flag is set.")
        if not self.vat_flag and self.vat_amount is not None:
            raise ValidationError("VAT amount should not be set if VAT flag is not set.")

        # Ensure trust transactions use a trust account and non-trust transactions do not
        is_trust_account = False # Default to False if account is not set
        if self.account_id: # <-- CHANGED TO THIS
            # Only try to access self.account if the ID is present
            is_trust_account = self.account.account_type == 'TRUST'
        else:
            # If account_id is None, it means the FK is not set.
            # Django's default form validation for required FKs will handle the error.
            pass

        if self.is_trust_transaction and not is_trust_account:
            raise ValidationError("Trust transactions must use a Trust account from Chart of Accounts.")
        elif not self.is_trust_transaction and is_trust_account:
            raise ValidationError("Non-trust transactions cannot use a Trust account from Chart of Accounts.")

        # Specific checks for transaction types vs. trust flag
        if self.transaction_type in ['TRUST_DEPOSIT', 'TRUST_DISBURSEMENT'] and not self.is_trust_transaction:
            raise ValidationError(f"Transaction type '{self.transaction_type}' requires 'is_trust_transaction' to be True.")
        elif self.transaction_type not in ['TRUST_DEPOSIT', 'TRUST_DISBURSEMENT'] and self.is_trust_transaction:
            raise ValidationError(f"Transaction type '{self.transaction_type}' cannot have 'is_trust_transaction' set to True.")


    def save(self, *args, **kwargs):
        self.full_clean() # Call full_clean to run all validation rules
        if self.vat_flag and self.vat_amount is None:
            try:
                # Calculate VAT based on current rate if not provided
                current_vat_rate = VatRate.objects.get_rate_for_date(self.transaction_date)
                self.vat_amount = self.amount * current_vat_rate
            except BusinessLogicError as e:
                raise BusinessLogicError(f"VAT calculation failed: {str(e)}")

        # Determine if it's a trust transaction based on account type
        # This line will only execute if self.account is set after full_clean()
        if self.account_id: # <-- CHANGED TO THIS
            self.is_trust_transaction = (self.account.account_type == 'TRUST')
        else:
            # If account_id is None, is_trust_transaction cannot be determined
            # based on account type. It should already be caught by validation.
            self.is_trust_transaction = False # Default if no account

        super().save(*args, **kwargs)

    def calculate_vat(self):
        if not self.vat_flag:
            return Decimal('0.00')
        if self.vat_amount is not None:
            return self.vat_amount

        try:
            current_vat_rate = VatRate.objects.get_rate_for_date(self.transaction_date)
            return self.amount * current_vat_rate
        except BusinessLogicError as e:
            # Re-raise as a more specific exception or handle appropriately
            raise BusinessLogicError(f"Failed to calculate VAT: {e}")

    def get_liability_account(self):
        try:
            return SystemAccount.active_objects.get(type='LIABILITY_PAYMENTS').account
        except SystemAccount.DoesNotExist:
            raise BusinessLogicError("Liability payments account not configured in System Accounts.")

    def get_asset_account(self):
        try:
            return SystemAccount.active_objects.get(type='ASSET_RECEIVABLES').account
        except SystemAccount.DoesNotExist:
            raise BusinessLogicError("Asset receivables account not configured in System Accounts.")

    def get_vat_liability_account(self):
        try:
            return SystemAccount.active_objects.get(type='VAT_LIABILITY').account
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
        client.save(update_fields=['income_ytd', 'expense_ytd', 'trust_balance'])
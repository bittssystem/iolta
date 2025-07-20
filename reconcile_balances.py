from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import Sum, Q
from decimal import Decimal
from iolat.models import Client, FinancialTransaction

class Command(BaseCommand):
    help = 'Reconcile client balances (income_ytd, expense_ytd, trust_balance) based on transactions.'

    def add_arguments(self, parser):
        parser.add_argument('--year', type=int, help='Year to reconcile (default: current year)')

    def handle(self, *args, **options):
        year = options.get('year', datetime.date.today().year)
        self.stdout.write(f"Reconciling client balances for {year}...")
        
        with transaction.atomic():
            for client in Client.active_objects.filter(is_active=True):
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
                try:
                    client.full_clean()
                    client.save()
                    self.stdout.write(self.style.SUCCESS(f"Reconciled balances for client: {client.name}"))
                except ValidationError as e:
                    self.stdout.write(self.style.ERROR(f"Validation error for client {client.name}: {e}"))
# coreblock/management/commands/create_sample_chartofaccounts.py

from django.core.management.base import BaseCommand
from django.db import transaction
from coreblock.models import ChartOfAccount # Ensure this import path is correct for your project

class Command(BaseCommand):
    help = 'Creates sample Chart of Account entries for testing.'

    def handle(self, *args, **options):
        self.stdout.write("Creating sample Chart of Account entries...")

        # Define the sample accounts
        sample_accounts = [
            {'code': '1000', 'name': 'Cash in Bank', 'account_type': 'ASSET'},
            {'code': '1200', 'name': 'Accounts Receivable', 'account_type': 'ASSET'},
            {'code': '2000', 'name': 'Accounts Payable', 'account_type': 'LIABILITY'},
            {'code': '2100', 'name': 'VAT Payable', 'account_type': 'LIABILITY'},
            {'code': '3000', 'name': 'Owner\'s Equity', 'account_type': 'EQUITY'},
            {'code': '4000', 'name': 'Service Revenue', 'account_type': 'REVENUE'},
            {'code': '5000', 'name': 'Rent Expense', 'account_type': 'EXPENSE'},
            {'code': '5100', 'name': 'Utilities Expense', 'account_type': 'EXPENSE'},
            {'code': '8000', 'name': 'Trust Funds Held', 'account_type': 'TRUST'},
            {'code': '8010', 'name': 'Trust Disbursements', 'account_type': 'TRUST'},
        ]

        with transaction.atomic():
            for acc_data in sample_accounts:
                account, created = ChartOfAccount.objects.get_or_create(
                    code=acc_data['code'],
                    defaults={
                        'name': acc_data['name'],
                        'account_type': acc_data['account_type'],
                        'is_active': True # Ensure they are active
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(
                        f"Successfully created ChartOfAccount: {account.name} ({account.code})"
                    ))
                else:
                    self.stdout.write(self.style.WARNING(
                        f"ChartOfAccount already exists: {account.name} ({account.code})"
                    ))

        self.stdout.write(self.style.SUCCESS("Finished creating sample Chart of Account entries."))
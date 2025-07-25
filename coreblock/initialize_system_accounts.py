from django.core.management.base import BaseCommand
from django.db import transaction
from iolat.models import ChartOfAccount, SystemAccount

class Command(BaseCommand):
    help = 'Initialize required system accounts for financial transactions.'

    def handle(self, *args, **options):
        with transaction.atomic():
            accounts = [
                {'code': 'LIAB001', 'name': 'Liability Payments', 'account_type': 'LIABILITY'},
                {'code': 'ASSET001', 'name': 'Asset Receivables', 'account_type': 'ASSET'},
                {'code': 'VAT001', 'name': 'VAT Liability', 'account_type': 'LIABILITY'},
                {'code': 'TRU001', 'name': 'Trust Account', 'account_type': 'TRUST'},
            ]
            for acc in accounts:
                chart_account, created = ChartOfAccount.objects.get_or_create(
                    code=acc['code'],
                    defaults={'name': acc['name'], 'account_type': acc['account_type']}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Created ChartOfAccount: {chart_account}"))
                else:
                    self.stdout.write(f"ChartOfAccount already exists: {chart_account}")

            system_accounts = [
                {'type': 'LIABILITY_PAYMENTS', 'account_code': 'LIAB001'},
                {'type': 'ASSET_RECEIVABLES', 'account_code': 'ASSET001'},
                {'type': 'VAT_LIABILITY', 'account_code': 'VAT001'},
                {'type': 'TRUST_ACCOUNT', 'account_code': 'TRU001'},
            ]
            for sys_acc in system_accounts:
                account = ChartOfAccount.objects.get(code=sys_acc['account_code'])
                system_account, created = SystemAccount.objects.get_or_create(
                    type=sys_acc['type'],
                    defaults={'account': account}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Created SystemAccount: {system_account}"))
                else:
                    self.stdout.write(f"SystemAccount already exists: {system_account}")
from django.core.management.base import BaseCommand
from django.db import transaction
from decimal import Decimal
from iolat.models import Client

class Command(BaseCommand):
    help = 'Reset year-to-date balances (income_ytd, expense_ytd) for all clients.'

    def add_arguments(self, parser):
        parser.add_argument('--year', type=int, help='Year to reset balances for (default: current year)')

    def handle(self, *args, **options):
        year = options.get('year', datetime.date.today().year)
        self.stdout.write(f"Resetting year-to-date balances for {year}...")
        
        with transaction.atomic():
            for client in Client.active_objects.filter(is_active=True):
                client.income_ytd = Decimal('0.00')
                client.expense_ytd = Decimal('0.00')
                try:
                    client.full_clean()
                    client.save()
                    self.stdout.write(self.style.SUCCESS(f"Reset balances for client: {client.name}"))
                except ValidationError as e:
                    self.stdout.write(self.style.ERROR(f"Validation error for client {client.name}: {e}"))
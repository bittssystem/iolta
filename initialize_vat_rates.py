from django.core.management.base import BaseCommand
from django.db import transaction
from decimal import Decimal
from iolat.models import VatRate
import datetime

class Command(BaseCommand):
    help = 'Initialize VAT rates with a default rate.'

    def handle(self, *args, **options):
        with transaction.atomic():
            vat_rate, created = VatRate.objects.get_or_create(
                rate=Decimal('0.15'),
                effective_from=datetime.date(2020, 1, 1),
                effective_to=None,
                defaults={'created_at': datetime.datetime.now()}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created VAT rate: {vat_rate}"))
            else:
                self.stdout.write(f"VAT rate already exists: {vat_rate}")
# coreblock/admin.py
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import (
    VatRate, SystemAccount, ChartOfAccount, Client, Employee,
    Creditor, Debtor, Matter, FinancialTransaction
)

# VatRate Admin
@admin.register(VatRate)
class VatRateAdmin(SimpleHistoryAdmin):
    list_display = ('rate', 'effective_from', 'effective_to', 'created_at')
    list_filter = ('effective_from', 'effective_to')
    search_fields = ('rate',)
    date_hierarchy = 'effective_from'
    ordering = ('-effective_from',)
    readonly_fields = ('created_at', 'updated_at')

    def get_queryset(self, request):
        return self.model.objects.all()


# SystemAccount Admin
@admin.register(SystemAccount)
class SystemAccountAdmin(SimpleHistoryAdmin):
    list_display = ('type', 'account', 'is_active', 'created_at')
    list_filter = ('type', 'is_active')
    search_fields = ('type', 'account__name', 'account__code')
    autocomplete_fields = ('account',)
    readonly_fields = ('created_at', 'updated_at')

    def get_queryset(self, request):
        return self.model.all_objects.all()


# ChartOfAccount Admin
@admin.register(ChartOfAccount)
class ChartOfAccountAdmin(SimpleHistoryAdmin):
    list_display = ('code', 'name', 'account_type', 'is_active', 'created_at')
    list_filter = ('account_type', 'is_active')
    search_fields = ('code', 'name')
    readonly_fields = ('created_at', 'updated_at')

    def get_queryset(self, request):
        return self.model.all_objects.all()


# FinancialTransactionInline (Only used for Matter, not Client)
class FinancialTransactionInline(admin.TabularInline):
    model = FinancialTransaction
    extra = 0
    fields = (
        'description', 'amount', 'transaction_type', 'transaction_date',
        'vat_flag', 'account', # 'is_trust_transaction' removed from fields
    )
    readonly_fields = ('created_at', 'updated_at', 'is_trust_transaction', 'vat_amount') # 'is_trust_transaction' and 'vat_amount' added to readonly_fields
    autocomplete_fields = ('account',) # Added autocomplete for account
    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_active=True)


# Client Admin
@admin.register(Client)
class ClientAdmin(SimpleHistoryAdmin):
    list_display = ('name', 'is_active', 'income_ytd', 'expense_ytd', 'trust_balance', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('income_ytd', 'expense_ytd', 'trust_balance', 'created_at', 'updated_at')

    def get_queryset(self, request):
        return self.model.all_objects.all()


# Employee Admin
@admin.register(Employee)
class EmployeeAdmin(SimpleHistoryAdmin):
    list_display = ('user', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('user__username',)
    readonly_fields = ('created_at', 'updated_at')

    def get_queryset(self, request):
        return self.model.all_objects.all()


# Creditor Admin
@admin.register(Creditor)
class CreditorAdmin(SimpleHistoryAdmin):
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')

    def get_queryset(self, request):
        return self.model.all_objects.all()


# Debtor Admin
@admin.register(Debtor)
class DebtorAdmin(SimpleHistoryAdmin):
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')

    def get_queryset(self, request):
        return self.model.all_objects.all()


# Financial Transaction Admin
@admin.register(FinancialTransaction)
class FinancialTransactionAdmin(SimpleHistoryAdmin):
    list_display = (
        'description', 'matter', 'amount', 'transaction_type', 'transaction_date',
        'recorded_by', 'vat_flag', 'is_trust_transaction', 'is_active', 'created_at'
    )
    list_filter = ('transaction_type', 'vat_flag', 'is_trust_transaction', 'is_active')
    search_fields = ('description', 'matter__description', 'matter__client__name')
    readonly_fields = ('created_at', 'updated_at')
    autocomplete_fields = ('recorded_by', 'account')
    show_change_link = True


    def get_queryset(self, request):
        return self.model.all_objects.all()


# Matter Admin
@admin.register(Matter)
class MatterAdmin(SimpleHistoryAdmin):
    list_display = (
        'description', 'client', 'matter_type', 'status', 'created_by', 'is_active', 'created_at'
    )
    list_filter = ('matter_type', 'status', 'is_active')
    search_fields = ('description', 'client__name')
    inlines = [FinancialTransactionInline]
    readonly_fields = ('created_at', 'updated_at')
    autocomplete_fields = ('client', 'created_by')

    def get_queryset(self, request):
        return self.model.all_objects.all()
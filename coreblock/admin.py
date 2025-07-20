from django.contrib import admin
from .models import (
    Client, Employee, Matter, FinancialTransaction, ChartOfAccount,
    Creditor, Debtor, SystemAccount, VatRate
)

class MatterInline(admin.TabularInline):
    model = Matter
    extra = 0
    fields = ('description', 'matter_type', 'status', 'is_active')
    show_change_link = True

class CreditorInline(admin.TabularInline):
    model = Creditor
    extra = 0
    fields = ('name', 'amount_owed', 'is_active')
    show_change_link = True

class DebtorInline(admin.TabularInline):
    model = Debtor
    extra = 0
    fields = ('name', 'amount_due', 'is_active')
    show_change_link = True

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'identity_number', 'registration_number', 'is_trust',
        'income_ytd', 'expense_ytd', 'trust_balance', 'is_active', 'created_at', 'updated_at'
    )
    list_filter = ('is_trust', 'is_active')
    search_fields = ('name', 'email', 'identity_number', 'registration_number')
    inlines = [MatterInline, CreditorInline, DebtorInline]
    readonly_fields = ('trust_balance', 'income_ytd', 'expense_ytd', 'created_at', 'updated_at')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'email')
    readonly_fields = ('created_at', 'updated_at')

class FinancialTransactionInline(admin.TabularInline):
    model = FinancialTransaction
    extra = 0
    fields = (
        'description', 'amount', 'transaction_type', 'transaction_date',
        'vat_flag', 'recorded_by', 'account', 'is_trust_transaction', 'is_active'
    )
    show_change_link = True

@admin.register(Matter)
class MatterAdmin(admin.ModelAdmin):
    list_display = (
        'description', 'client', 'matter_type', 'status', 'is_active', 'created_at', 'updated_at'
    )
    list_filter = ('matter_type', 'status', 'is_active')
    search_fields = ('description',)
    inlines = [FinancialTransactionInline]
    readonly_fields = ('created_at', 'updated_at')

@admin.register(FinancialTransaction)
class FinancialTransactionAdmin(admin.ModelAdmin):
    list_display = (
        'description', 'matter', 'amount', 'transaction_type', 'transaction_date',
        'vat_flag', 'recorded_by', 'account', 'is_trust_transaction', 'is_active', 'created_at', 'updated_at'
    )
    list_filter = (
        'transaction_type', 'vat_flag', 'is_trust_transaction', 'is_active', 'transaction_date'
    )
    search_fields = ('description',)
    autocomplete_fields = ['matter', 'recorded_by', 'account']
    readonly_fields = ('created_at', 'updated_at')

@admin.register(ChartOfAccount)
class ChartOfAccountAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'account_type', 'is_active', 'created_at', 'updated_at')
    list_filter = ('account_type', 'is_active')
    search_fields = ('code', 'name')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Creditor)
class CreditorAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount_owed', 'client', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('name',)
    autocomplete_fields = ['client']
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Debtor)
class DebtorAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount_due', 'client', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('name',)
    autocomplete_fields = ['client']
    readonly_fields = ('created_at', 'updated_at')

@admin.register(SystemAccount)
class SystemAccountAdmin(admin.ModelAdmin):
    list_display = ('type', 'account', 'is_active', 'created_at', 'updated_at')
    list_filter = ('type', 'is_active')
    search_fields = ('type',)
    autocomplete_fields = ['account']
    readonly_fields = ('created_at', 'updated_at')

@admin.register(VatRate)
class VatRateAdmin(admin.ModelAdmin):
    list_display = ('rate', 'effective_from', 'effective_to', 'created_at', 'updated_at')
    search_fields = ('rate',)
    list_filter = ('effective_from', 'effective_to')
    readonly_fields = ('created_at', 'updated_at')
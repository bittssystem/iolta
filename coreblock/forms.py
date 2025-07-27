from django import forms
from . import models

class VatRateForm(forms.ModelForm):
    class Meta:
        model = models.VatRate
        fields = '__all__'

class SystemAccountForm(forms.ModelForm):
    class Meta:
        model = models.SystemAccount
        fields = '__all__'

class ChartOfAccountForm(forms.ModelForm):
    class Meta:
        model = models.ChartOfAccount
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = '__all__'

class CreditorForm(forms.ModelForm):
    class Meta:
        model = models.Creditor
        fields = '__all__'

class DebtorForm(forms.ModelForm):
    class Meta:
        model = models.Debtor
        fields = '__all__'

class MatterForm(forms.ModelForm):
    class Meta:
        model = models.Matter
        fields = '__all__'

class FinancialTransactionForm(forms.ModelForm):
    class Meta:
        model = models.FinancialTransaction
        fields = '__all__'
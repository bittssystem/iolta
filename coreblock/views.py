from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class ChartOfAccountListView(generic.ListView):
    model = models.ChartOfAccount
    form_class = forms.ChartOfAccountForm


class ChartOfAccountCreateView(generic.CreateView):
    model = models.ChartOfAccount
    form_class = forms.ChartOfAccountForm


class ChartOfAccountDetailView(generic.DetailView):
    model = models.ChartOfAccount
    form_class = forms.ChartOfAccountForm


class ChartOfAccountUpdateView(generic.UpdateView):
    model = models.ChartOfAccount
    form_class = forms.ChartOfAccountForm
    pk_url_kwarg = "pk"


class ChartOfAccountDeleteView(generic.DeleteView):
    model = models.ChartOfAccount
    success_url = reverse_lazy("coreblock_ChartOfAccount_list")


class ClientListView(generic.ListView):
    model = models.Client
    form_class = forms.ClientForm


class ClientCreateView(generic.CreateView):
    model = models.Client
    form_class = forms.ClientForm


class ClientDetailView(generic.DetailView):
    model = models.Client
    form_class = forms.ClientForm


class ClientUpdateView(generic.UpdateView):
    model = models.Client
    form_class = forms.ClientForm
    pk_url_kwarg = "pk"


class ClientDeleteView(generic.DeleteView):
    model = models.Client
    success_url = reverse_lazy("coreblock_Client_list")


class CreditorListView(generic.ListView):
    model = models.Creditor
    form_class = forms.CreditorForm


class CreditorCreateView(generic.CreateView):
    model = models.Creditor
    form_class = forms.CreditorForm


class CreditorDetailView(generic.DetailView):
    model = models.Creditor
    form_class = forms.CreditorForm


class CreditorUpdateView(generic.UpdateView):
    model = models.Creditor
    form_class = forms.CreditorForm
    pk_url_kwarg = "pk"


class CreditorDeleteView(generic.DeleteView):
    model = models.Creditor
    success_url = reverse_lazy("coreblock_Creditor_list")


class DebtorListView(generic.ListView):
    model = models.Debtor
    form_class = forms.DebtorForm


class DebtorCreateView(generic.CreateView):
    model = models.Debtor
    form_class = forms.DebtorForm


class DebtorDetailView(generic.DetailView):
    model = models.Debtor
    form_class = forms.DebtorForm


class DebtorUpdateView(generic.UpdateView):
    model = models.Debtor
    form_class = forms.DebtorForm
    pk_url_kwarg = "pk"


class DebtorDeleteView(generic.DeleteView):
    model = models.Debtor
    success_url = reverse_lazy("coreblock_Debtor_list")


class EmployeeListView(generic.ListView):
    model = models.Employee
    form_class = forms.EmployeeForm


class EmployeeCreateView(generic.CreateView):
    model = models.Employee
    form_class = forms.EmployeeForm


class EmployeeDetailView(generic.DetailView):
    model = models.Employee
    form_class = forms.EmployeeForm


class EmployeeUpdateView(generic.UpdateView):
    model = models.Employee
    form_class = forms.EmployeeForm
    pk_url_kwarg = "pk"


class EmployeeDeleteView(generic.DeleteView):
    model = models.Employee
    success_url = reverse_lazy("coreblock_Employee_list")


class FinancialTransactionListView(generic.ListView):
    model = models.FinancialTransaction
    form_class = forms.FinancialTransactionForm


class FinancialTransactionCreateView(generic.CreateView):
    model = models.FinancialTransaction
    form_class = forms.FinancialTransactionForm


class FinancialTransactionDetailView(generic.DetailView):
    model = models.FinancialTransaction
    form_class = forms.FinancialTransactionForm


class FinancialTransactionUpdateView(generic.UpdateView):
    model = models.FinancialTransaction
    form_class = forms.FinancialTransactionForm
    pk_url_kwarg = "pk"


class FinancialTransactionDeleteView(generic.DeleteView):
    model = models.FinancialTransaction
    success_url = reverse_lazy("coreblock_FinancialTransaction_list")


class MatterListView(generic.ListView):
    model = models.Matter
    form_class = forms.MatterForm


class MatterCreateView(generic.CreateView):
    model = models.Matter
    form_class = forms.MatterForm


class MatterDetailView(generic.DetailView):
    model = models.Matter
    form_class = forms.MatterForm


class MatterUpdateView(generic.UpdateView):
    model = models.Matter
    form_class = forms.MatterForm
    pk_url_kwarg = "pk"


class MatterDeleteView(generic.DeleteView):
    model = models.Matter
    success_url = reverse_lazy("coreblock_Matter_list")


class SystemAccountListView(generic.ListView):
    model = models.SystemAccount
    form_class = forms.SystemAccountForm


class SystemAccountCreateView(generic.CreateView):
    model = models.SystemAccount
    form_class = forms.SystemAccountForm


class SystemAccountDetailView(generic.DetailView):
    model = models.SystemAccount
    form_class = forms.SystemAccountForm


class SystemAccountUpdateView(generic.UpdateView):
    model = models.SystemAccount
    form_class = forms.SystemAccountForm
    pk_url_kwarg = "pk"


class SystemAccountDeleteView(generic.DeleteView):
    model = models.SystemAccount
    success_url = reverse_lazy("coreblock_SystemAccount_list")


class VatRateListView(generic.ListView):
    model = models.VatRate
    form_class = forms.VatRateForm


class VatRateCreateView(generic.CreateView):
    model = models.VatRate
    form_class = forms.VatRateForm


class VatRateDetailView(generic.DetailView):
    model = models.VatRate
    form_class = forms.VatRateForm


class VatRateUpdateView(generic.UpdateView):
    model = models.VatRate
    form_class = forms.VatRateForm
    pk_url_kwarg = "pk"


class VatRateDeleteView(generic.DeleteView):
    model = models.VatRate
    success_url = reverse_lazy("coreblock_VatRate_list")
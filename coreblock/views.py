from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class ActiveManagerListView(generic.ListView):
    model = models.ActiveManager
    form_class = forms.ActiveManagerForm


class ActiveManagerCreateView(generic.CreateView):
    model = models.ActiveManager
    form_class = forms.ActiveManagerForm


class ActiveManagerDetailView(generic.DetailView):
    model = models.ActiveManager
    form_class = forms.ActiveManagerForm


class ActiveManagerUpdateView(generic.UpdateView):
    model = models.ActiveManager
    form_class = forms.ActiveManagerForm
    pk_url_kwarg = "pk"


class ActiveManagerDeleteView(generic.DeleteView):
    model = models.ActiveManager
    success_url = reverse_lazy("coreblock_ActiveManager_list")


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


class ChartOfAccountManagerListView(generic.ListView):
    model = models.ChartOfAccountManager
    form_class = forms.ChartOfAccountManagerForm


class ChartOfAccountManagerCreateView(generic.CreateView):
    model = models.ChartOfAccountManager
    form_class = forms.ChartOfAccountManagerForm


class ChartOfAccountManagerDetailView(generic.DetailView):
    model = models.ChartOfAccountManager
    form_class = forms.ChartOfAccountManagerForm


class ChartOfAccountManagerUpdateView(generic.UpdateView):
    model = models.ChartOfAccountManager
    form_class = forms.ChartOfAccountManagerForm
    pk_url_kwarg = "pk"


class ChartOfAccountManagerDeleteView(generic.DeleteView):
    model = models.ChartOfAccountManager
    success_url = reverse_lazy("coreblock_ChartOfAccountManager_list")


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


class ClientManagerListView(generic.ListView):
    model = models.ClientManager
    form_class = forms.ClientManagerForm


class ClientManagerCreateView(generic.CreateView):
    model = models.ClientManager
    form_class = forms.ClientManagerForm


class ClientManagerDetailView(generic.DetailView):
    model = models.ClientManager
    form_class = forms.ClientManagerForm


class ClientManagerUpdateView(generic.UpdateView):
    model = models.ClientManager
    form_class = forms.ClientManagerForm
    pk_url_kwarg = "pk"


class ClientManagerDeleteView(generic.DeleteView):
    model = models.ClientManager
    success_url = reverse_lazy("coreblock_ClientManager_list")


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


class CreditorManagerListView(generic.ListView):
    model = models.CreditorManager
    form_class = forms.CreditorManagerForm


class CreditorManagerCreateView(generic.CreateView):
    model = models.CreditorManager
    form_class = forms.CreditorManagerForm


class CreditorManagerDetailView(generic.DetailView):
    model = models.CreditorManager
    form_class = forms.CreditorManagerForm


class CreditorManagerUpdateView(generic.UpdateView):
    model = models.CreditorManager
    form_class = forms.CreditorManagerForm
    pk_url_kwarg = "pk"


class CreditorManagerDeleteView(generic.DeleteView):
    model = models.CreditorManager
    success_url = reverse_lazy("coreblock_CreditorManager_list")


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


class DebtorManagerListView(generic.ListView):
    model = models.DebtorManager
    form_class = forms.DebtorManagerForm


class DebtorManagerCreateView(generic.CreateView):
    model = models.DebtorManager
    form_class = forms.DebtorManagerForm


class DebtorManagerDetailView(generic.DetailView):
    model = models.DebtorManager
    form_class = forms.DebtorManagerForm


class DebtorManagerUpdateView(generic.UpdateView):
    model = models.DebtorManager
    form_class = forms.DebtorManagerForm
    pk_url_kwarg = "pk"


class DebtorManagerDeleteView(generic.DeleteView):
    model = models.DebtorManager
    success_url = reverse_lazy("coreblock_DebtorManager_list")


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


class EmployeeManagerListView(generic.ListView):
    model = models.EmployeeManager
    form_class = forms.EmployeeManagerForm


class EmployeeManagerCreateView(generic.CreateView):
    model = models.EmployeeManager
    form_class = forms.EmployeeManagerForm


class EmployeeManagerDetailView(generic.DetailView):
    model = models.EmployeeManager
    form_class = forms.EmployeeManagerForm


class EmployeeManagerUpdateView(generic.UpdateView):
    model = models.EmployeeManager
    form_class = forms.EmployeeManagerForm
    pk_url_kwarg = "pk"


class EmployeeManagerDeleteView(generic.DeleteView):
    model = models.EmployeeManager
    success_url = reverse_lazy("coreblock_EmployeeManager_list")


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


class FinancialTransactionManagerListView(generic.ListView):
    model = models.FinancialTransactionManager
    form_class = forms.FinancialTransactionManagerForm


class FinancialTransactionManagerCreateView(generic.CreateView):
    model = models.FinancialTransactionManager
    form_class = forms.FinancialTransactionManagerForm


class FinancialTransactionManagerDetailView(generic.DetailView):
    model = models.FinancialTransactionManager
    form_class = forms.FinancialTransactionManagerForm


class FinancialTransactionManagerUpdateView(generic.UpdateView):
    model = models.FinancialTransactionManager
    form_class = forms.FinancialTransactionManagerForm
    pk_url_kwarg = "pk"


class FinancialTransactionManagerDeleteView(generic.DeleteView):
    model = models.FinancialTransactionManager
    success_url = reverse_lazy("coreblock_FinancialTransactionManager_list")


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


class MatterManagerListView(generic.ListView):
    model = models.MatterManager
    form_class = forms.MatterManagerForm


class MatterManagerCreateView(generic.CreateView):
    model = models.MatterManager
    form_class = forms.MatterManagerForm


class MatterManagerDetailView(generic.DetailView):
    model = models.MatterManager
    form_class = forms.MatterManagerForm


class MatterManagerUpdateView(generic.UpdateView):
    model = models.MatterManager
    form_class = forms.MatterManagerForm
    pk_url_kwarg = "pk"


class MatterManagerDeleteView(generic.DeleteView):
    model = models.MatterManager
    success_url = reverse_lazy("coreblock_MatterManager_list")


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


class VatRateManagerListView(generic.ListView):
    model = models.VatRateManager
    form_class = forms.VatRateManagerForm


class VatRateManagerCreateView(generic.CreateView):
    model = models.VatRateManager
    form_class = forms.VatRateManagerForm


class VatRateManagerDetailView(generic.DetailView):
    model = models.VatRateManager
    form_class = forms.VatRateManagerForm


class VatRateManagerUpdateView(generic.UpdateView):
    model = models.VatRateManager
    form_class = forms.VatRateManagerForm
    pk_url_kwarg = "pk"


class VatRateManagerDeleteView(generic.DeleteView):
    model = models.VatRateManager
    success_url = reverse_lazy("coreblock_VatRateManager_list")

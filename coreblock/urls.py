from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("ActiveManager", api.ActiveManagerViewSet)
router.register("ChartOfAccount", api.ChartOfAccountViewSet)
router.register("ChartOfAccountManager", api.ChartOfAccountManagerViewSet)
router.register("Client", api.ClientViewSet)
router.register("ClientManager", api.ClientManagerViewSet)
router.register("Creditor", api.CreditorViewSet)
router.register("CreditorManager", api.CreditorManagerViewSet)
router.register("Debtor", api.DebtorViewSet)
router.register("DebtorManager", api.DebtorManagerViewSet)
router.register("Employee", api.EmployeeViewSet)
router.register("EmployeeManager", api.EmployeeManagerViewSet)
router.register("FinancialTransaction", api.FinancialTransactionViewSet)
router.register("FinancialTransactionManager", api.FinancialTransactionManagerViewSet)
router.register("Matter", api.MatterViewSet)
router.register("MatterManager", api.MatterManagerViewSet)
router.register("SystemAccount", api.SystemAccountViewSet)
router.register("VatRate", api.VatRateViewSet)
router.register("VatRateManager", api.VatRateManagerViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("coreblock/ActiveManager/", views.ActiveManagerListView.as_view(), name="coreblock_ActiveManager_list"),
    path("coreblock/ActiveManager/create/", views.ActiveManagerCreateView.as_view(), name="coreblock_ActiveManager_create"),
    path("coreblock/ActiveManager/detail/<int:pk>/", views.ActiveManagerDetailView.as_view(), name="coreblock_ActiveManager_detail"),
    path("coreblock/ActiveManager/update/<int:pk>/", views.ActiveManagerUpdateView.as_view(), name="coreblock_ActiveManager_update"),
    path("coreblock/ActiveManager/delete/<int:pk>/", views.ActiveManagerDeleteView.as_view(), name="coreblock_ActiveManager_delete"),
    path("coreblock/ChartOfAccount/", views.ChartOfAccountListView.as_view(), name="coreblock_ChartOfAccount_list"),
    path("coreblock/ChartOfAccount/create/", views.ChartOfAccountCreateView.as_view(), name="coreblock_ChartOfAccount_create"),
    path("coreblock/ChartOfAccount/detail/<int:pk>/", views.ChartOfAccountDetailView.as_view(), name="coreblock_ChartOfAccount_detail"),
    path("coreblock/ChartOfAccount/update/<int:pk>/", views.ChartOfAccountUpdateView.as_view(), name="coreblock_ChartOfAccount_update"),
    path("coreblock/ChartOfAccount/delete/<int:pk>/", views.ChartOfAccountDeleteView.as_view(), name="coreblock_ChartOfAccount_delete"),
    path("coreblock/ChartOfAccountManager/", views.ChartOfAccountManagerListView.as_view(), name="coreblock_ChartOfAccountManager_list"),
    path("coreblock/ChartOfAccountManager/create/", views.ChartOfAccountManagerCreateView.as_view(), name="coreblock_ChartOfAccountManager_create"),
    path("coreblock/ChartOfAccountManager/detail/<int:pk>/", views.ChartOfAccountManagerDetailView.as_view(), name="coreblock_ChartOfAccountManager_detail"),
    path("coreblock/ChartOfAccountManager/update/<int:pk>/", views.ChartOfAccountManagerUpdateView.as_view(), name="coreblock_ChartOfAccountManager_update"),
    path("coreblock/ChartOfAccountManager/delete/<int:pk>/", views.ChartOfAccountManagerDeleteView.as_view(), name="coreblock_ChartOfAccountManager_delete"),
    path("coreblock/Client/", views.ClientListView.as_view(), name="coreblock_Client_list"),
    path("coreblock/Client/create/", views.ClientCreateView.as_view(), name="coreblock_Client_create"),
    path("coreblock/Client/detail/<int:pk>/", views.ClientDetailView.as_view(), name="coreblock_Client_detail"),
    path("coreblock/Client/update/<int:pk>/", views.ClientUpdateView.as_view(), name="coreblock_Client_update"),
    path("coreblock/Client/delete/<int:pk>/", views.ClientDeleteView.as_view(), name="coreblock_Client_delete"),
    path("coreblock/ClientManager/", views.ClientManagerListView.as_view(), name="coreblock_ClientManager_list"),
    path("coreblock/ClientManager/create/", views.ClientManagerCreateView.as_view(), name="coreblock_ClientManager_create"),
    path("coreblock/ClientManager/detail/<int:pk>/", views.ClientManagerDetailView.as_view(), name="coreblock_ClientManager_detail"),
    path("coreblock/ClientManager/update/<int:pk>/", views.ClientManagerUpdateView.as_view(), name="coreblock_ClientManager_update"),
    path("coreblock/ClientManager/delete/<int:pk>/", views.ClientManagerDeleteView.as_view(), name="coreblock_ClientManager_delete"),
    path("coreblock/Creditor/", views.CreditorListView.as_view(), name="coreblock_Creditor_list"),
    path("coreblock/Creditor/create/", views.CreditorCreateView.as_view(), name="coreblock_Creditor_create"),
    path("coreblock/Creditor/detail/<int:pk>/", views.CreditorDetailView.as_view(), name="coreblock_Creditor_detail"),
    path("coreblock/Creditor/update/<int:pk>/", views.CreditorUpdateView.as_view(), name="coreblock_Creditor_update"),
    path("coreblock/Creditor/delete/<int:pk>/", views.CreditorDeleteView.as_view(), name="coreblock_Creditor_delete"),
    path("coreblock/CreditorManager/", views.CreditorManagerListView.as_view(), name="coreblock_CreditorManager_list"),
    path("coreblock/CreditorManager/create/", views.CreditorManagerCreateView.as_view(), name="coreblock_CreditorManager_create"),
    path("coreblock/CreditorManager/detail/<int:pk>/", views.CreditorManagerDetailView.as_view(), name="coreblock_CreditorManager_detail"),
    path("coreblock/CreditorManager/update/<int:pk>/", views.CreditorManagerUpdateView.as_view(), name="coreblock_CreditorManager_update"),
    path("coreblock/CreditorManager/delete/<int:pk>/", views.CreditorManagerDeleteView.as_view(), name="coreblock_CreditorManager_delete"),
    path("coreblock/Debtor/", views.DebtorListView.as_view(), name="coreblock_Debtor_list"),
    path("coreblock/Debtor/create/", views.DebtorCreateView.as_view(), name="coreblock_Debtor_create"),
    path("coreblock/Debtor/detail/<int:pk>/", views.DebtorDetailView.as_view(), name="coreblock_Debtor_detail"),
    path("coreblock/Debtor/update/<int:pk>/", views.DebtorUpdateView.as_view(), name="coreblock_Debtor_update"),
    path("coreblock/Debtor/delete/<int:pk>/", views.DebtorDeleteView.as_view(), name="coreblock_Debtor_delete"),
    path("coreblock/DebtorManager/", views.DebtorManagerListView.as_view(), name="coreblock_DebtorManager_list"),
    path("coreblock/DebtorManager/create/", views.DebtorManagerCreateView.as_view(), name="coreblock_DebtorManager_create"),
    path("coreblock/DebtorManager/detail/<int:pk>/", views.DebtorManagerDetailView.as_view(), name="coreblock_DebtorManager_detail"),
    path("coreblock/DebtorManager/update/<int:pk>/", views.DebtorManagerUpdateView.as_view(), name="coreblock_DebtorManager_update"),
    path("coreblock/DebtorManager/delete/<int:pk>/", views.DebtorManagerDeleteView.as_view(), name="coreblock_DebtorManager_delete"),
    path("coreblock/Employee/", views.EmployeeListView.as_view(), name="coreblock_Employee_list"),
    path("coreblock/Employee/create/", views.EmployeeCreateView.as_view(), name="coreblock_Employee_create"),
    path("coreblock/Employee/detail/<int:pk>/", views.EmployeeDetailView.as_view(), name="coreblock_Employee_detail"),
    path("coreblock/Employee/update/<int:pk>/", views.EmployeeUpdateView.as_view(), name="coreblock_Employee_update"),
    path("coreblock/Employee/delete/<int:pk>/", views.EmployeeDeleteView.as_view(), name="coreblock_Employee_delete"),
    path("coreblock/EmployeeManager/", views.EmployeeManagerListView.as_view(), name="coreblock_EmployeeManager_list"),
    path("coreblock/EmployeeManager/create/", views.EmployeeManagerCreateView.as_view(), name="coreblock_EmployeeManager_create"),
    path("coreblock/EmployeeManager/detail/<int:pk>/", views.EmployeeManagerDetailView.as_view(), name="coreblock_EmployeeManager_detail"),
    path("coreblock/EmployeeManager/update/<int:pk>/", views.EmployeeManagerUpdateView.as_view(), name="coreblock_EmployeeManager_update"),
    path("coreblock/EmployeeManager/delete/<int:pk>/", views.EmployeeManagerDeleteView.as_view(), name="coreblock_EmployeeManager_delete"),
    path("coreblock/FinancialTransaction/", views.FinancialTransactionListView.as_view(), name="coreblock_FinancialTransaction_list"),
    path("coreblock/FinancialTransaction/create/", views.FinancialTransactionCreateView.as_view(), name="coreblock_FinancialTransaction_create"),
    path("coreblock/FinancialTransaction/detail/<int:pk>/", views.FinancialTransactionDetailView.as_view(), name="coreblock_FinancialTransaction_detail"),
    path("coreblock/FinancialTransaction/update/<int:pk>/", views.FinancialTransactionUpdateView.as_view(), name="coreblock_FinancialTransaction_update"),
    path("coreblock/FinancialTransaction/delete/<int:pk>/", views.FinancialTransactionDeleteView.as_view(), name="coreblock_FinancialTransaction_delete"),
    path("coreblock/FinancialTransactionManager/", views.FinancialTransactionManagerListView.as_view(), name="coreblock_FinancialTransactionManager_list"),
    path("coreblock/FinancialTransactionManager/create/", views.FinancialTransactionManagerCreateView.as_view(), name="coreblock_FinancialTransactionManager_create"),
    path("coreblock/FinancialTransactionManager/detail/<int:pk>/", views.FinancialTransactionManagerDetailView.as_view(), name="coreblock_FinancialTransactionManager_detail"),
    path("coreblock/FinancialTransactionManager/update/<int:pk>/", views.FinancialTransactionManagerUpdateView.as_view(), name="coreblock_FinancialTransactionManager_update"),
    path("coreblock/FinancialTransactionManager/delete/<int:pk>/", views.FinancialTransactionManagerDeleteView.as_view(), name="coreblock_FinancialTransactionManager_delete"),
    path("coreblock/Matter/", views.MatterListView.as_view(), name="coreblock_Matter_list"),
    path("coreblock/Matter/create/", views.MatterCreateView.as_view(), name="coreblock_Matter_create"),
    path("coreblock/Matter/detail/<int:pk>/", views.MatterDetailView.as_view(), name="coreblock_Matter_detail"),
    path("coreblock/Matter/update/<int:pk>/", views.MatterUpdateView.as_view(), name="coreblock_Matter_update"),
    path("coreblock/Matter/delete/<int:pk>/", views.MatterDeleteView.as_view(), name="coreblock_Matter_delete"),
    path("coreblock/MatterManager/", views.MatterManagerListView.as_view(), name="coreblock_MatterManager_list"),
    path("coreblock/MatterManager/create/", views.MatterManagerCreateView.as_view(), name="coreblock_MatterManager_create"),
    path("coreblock/MatterManager/detail/<int:pk>/", views.MatterManagerDetailView.as_view(), name="coreblock_MatterManager_detail"),
    path("coreblock/MatterManager/update/<int:pk>/", views.MatterManagerUpdateView.as_view(), name="coreblock_MatterManager_update"),
    path("coreblock/MatterManager/delete/<int:pk>/", views.MatterManagerDeleteView.as_view(), name="coreblock_MatterManager_delete"),
    path("coreblock/SystemAccount/", views.SystemAccountListView.as_view(), name="coreblock_SystemAccount_list"),
    path("coreblock/SystemAccount/create/", views.SystemAccountCreateView.as_view(), name="coreblock_SystemAccount_create"),
    path("coreblock/SystemAccount/detail/<int:pk>/", views.SystemAccountDetailView.as_view(), name="coreblock_SystemAccount_detail"),
    path("coreblock/SystemAccount/update/<int:pk>/", views.SystemAccountUpdateView.as_view(), name="coreblock_SystemAccount_update"),
    path("coreblock/SystemAccount/delete/<int:pk>/", views.SystemAccountDeleteView.as_view(), name="coreblock_SystemAccount_delete"),
    path("coreblock/VatRate/", views.VatRateListView.as_view(), name="coreblock_VatRate_list"),
    path("coreblock/VatRate/create/", views.VatRateCreateView.as_view(), name="coreblock_VatRate_create"),
    path("coreblock/VatRate/detail/<int:pk>/", views.VatRateDetailView.as_view(), name="coreblock_VatRate_detail"),
    path("coreblock/VatRate/update/<int:pk>/", views.VatRateUpdateView.as_view(), name="coreblock_VatRate_update"),
    path("coreblock/VatRate/delete/<int:pk>/", views.VatRateDeleteView.as_view(), name="coreblock_VatRate_delete"),
    path("coreblock/VatRateManager/", views.VatRateManagerListView.as_view(), name="coreblock_VatRateManager_list"),
    path("coreblock/VatRateManager/create/", views.VatRateManagerCreateView.as_view(), name="coreblock_VatRateManager_create"),
    path("coreblock/VatRateManager/detail/<int:pk>/", views.VatRateManagerDetailView.as_view(), name="coreblock_VatRateManager_detail"),
    path("coreblock/VatRateManager/update/<int:pk>/", views.VatRateManagerUpdateView.as_view(), name="coreblock_VatRateManager_update"),
    path("coreblock/VatRateManager/delete/<int:pk>/", views.VatRateManagerDeleteView.as_view(), name="coreblock_VatRateManager_delete"),

)

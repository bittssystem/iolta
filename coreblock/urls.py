from django.urls import path, include

from . import api
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("ChartOfAccount", api.ChartOfAccountViewSet)
router.register("Client", api.ClientViewSet)
router.register("Creditor", api.CreditorViewSet)
router.register("Debtor", api.DebtorViewSet)
router.register("Employee", api.EmployeeViewSet)
router.register("FinancialTransaction", api.FinancialTransactionViewSet)
router.register("Matter", api.MatterViewSet)
router.register("SystemAccount", api.SystemAccountViewSet)
router.register("VatRate", api.VatRateViewSet)


urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("coreblock/ChartOfAccount/", views.ChartOfAccountListView.as_view(), name="coreblock_ChartOfAccount_list"),
    path("coreblock/ChartOfAccount/create/", views.ChartOfAccountCreateView.as_view(), name="coreblock_ChartOfAccount_create"),
    path("coreblock/ChartOfAccount/detail/<int:pk>/", views.ChartOfAccountDetailView.as_view(), name="coreblock_ChartOfAccount_detail"),
    path("coreblock/ChartOfAccount/update/<int:pk>/", views.ChartOfAccountUpdateView.as_view(), name="coreblock_ChartOfAccount_update"),
    path("coreblock/ChartOfAccount/delete/<int:pk>/", views.ChartOfAccountDeleteView.as_view(), name="coreblock_ChartOfAccount_delete"),
    path("coreblock/Client/", views.ClientListView.as_view(), name="coreblock_Client_list"),
    path("coreblock/Client/create/", views.ClientCreateView.as_view(), name="coreblock_Client_create"),
    path("coreblock/Client/detail/<int:pk>/", views.ClientDetailView.as_view(), name="coreblock_Client_detail"),
    path("coreblock/Client/update/<int:pk>/", views.ClientUpdateView.as_view(), name="coreblock_Client_update"),
    path("coreblock/Client/delete/<int:pk>/", views.ClientDeleteView.as_view(), name="coreblock_Client_delete"),
    path("coreblock/Creditor/", views.CreditorListView.as_view(), name="coreblock_Creditor_list"),
    path("coreblock/Creditor/create/", views.CreditorCreateView.as_view(), name="coreblock_Creditor_create"),
    path("coreblock/Creditor/detail/<int:pk>/", views.CreditorDetailView.as_view(), name="coreblock_Creditor_detail"),
    path("coreblock/Creditor/update/<int:pk>/", views.CreditorUpdateView.as_view(), name="coreblock_Creditor_update"),
    path("coreblock/Creditor/delete/<int:pk>/", views.CreditorDeleteView.as_view(), name="coreblock_Creditor_delete"),
    path("coreblock/Debtor/", views.DebtorListView.as_view(), name="coreblock_Debtor_list"),
    path("coreblock/Debtor/create/", views.DebtorCreateView.as_view(), name="coreblock_Debtor_create"),
    path("coreblock/Debtor/detail/<int:pk>/", views.DebtorDetailView.as_view(), name="coreblock_Debtor_detail"),
    path("coreblock/Debtor/update/<int:pk>/", views.DebtorUpdateView.as_view(), name="coreblock_Debtor_update"),
    path("coreblock/Debtor/delete/<int:pk>/", views.DebtorDeleteView.as_view(), name="coreblock_Debtor_delete"),
    path("coreblock/Employee/", views.EmployeeListView.as_view(), name="coreblock_Employee_list"),
    path("coreblock/Employee/create/", views.EmployeeCreateView.as_view(), name="coreblock_Employee_create"),
    path("coreblock/Employee/detail/<int:pk>/", views.EmployeeDetailView.as_view(), name="coreblock_Employee_detail"),
    path("coreblock/Employee/update/<int:pk>/", views.EmployeeUpdateView.as_view(), name="coreblock_Employee_update"),
    path("coreblock/Employee/delete/<int:pk>/", views.EmployeeDeleteView.as_view(), name="coreblock_Employee_delete"),
    path("coreblock/FinancialTransaction/", views.FinancialTransactionListView.as_view(), name="coreblock_FinancialTransaction_list"),
    path("coreblock/FinancialTransaction/create/", views.FinancialTransactionCreateView.as_view(), name="coreblock_FinancialTransaction_create"),
    path("coreblock/FinancialTransaction/detail/<int:pk>/", views.FinancialTransactionDetailView.as_view(), name="coreblock_FinancialTransaction_detail"),
    path("coreblock/FinancialTransaction/update/<int:pk>/", views.FinancialTransactionUpdateView.as_view(), name="coreblock_FinancialTransaction_update"),
    path("coreblock/FinancialTransaction/delete/<int:pk>/", views.FinancialTransactionDeleteView.as_view(), name="coreblock_FinancialTransaction_delete"),
    path("coreblock/Matter/", views.MatterListView.as_view(), name="coreblock_Matter_list"),
    path("coreblock/Matter/create/", views.MatterCreateView.as_view(), name="coreblock_Matter_create"),
    path("coreblock/Matter/detail/<int:pk>/", views.MatterDetailView.as_view(), name="coreblock_Matter_detail"),
    path("coreblock/Matter/update/<int:pk>/", views.MatterUpdateView.as_view(), name="coreblock_Matter_update"),
    path("coreblock/Matter/delete/<int:pk>/", views.MatterDeleteView.as_view(), name="coreblock_Matter_delete"),
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
)
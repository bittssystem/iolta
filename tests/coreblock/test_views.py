import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_ActiveManager_list_view(client):
    instance1 = test_helpers.create_coreblock_ActiveManager()
    instance2 = test_helpers.create_coreblock_ActiveManager()
    url = reverse("coreblock_ActiveManager_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_ActiveManager_create_view(client):
    url = reverse("coreblock_ActiveManager_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ActiveManager_detail_view(client):
    instance = test_helpers.create_coreblock_ActiveManager()
    url = reverse("coreblock_ActiveManager_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_ActiveManager_update_view(client):
    instance = test_helpers.create_coreblock_ActiveManager()
    url = reverse("coreblock_ActiveManager_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ChartOfAccount_list_view(client):
    instance1 = test_helpers.create_coreblock_ChartOfAccount()
    instance2 = test_helpers.create_coreblock_ChartOfAccount()
    url = reverse("coreblock_ChartOfAccount_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_ChartOfAccount_create_view(client):
    url = reverse("coreblock_ChartOfAccount_create")
    data = {
        "code": "text",
        "name": "text",
        "account_type": "text",
        "is_active": True,
        "deleted_at": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ChartOfAccount_detail_view(client):
    instance = test_helpers.create_coreblock_ChartOfAccount()
    url = reverse("coreblock_ChartOfAccount_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_ChartOfAccount_update_view(client):
    instance = test_helpers.create_coreblock_ChartOfAccount()
    url = reverse("coreblock_ChartOfAccount_update", args=[instance.pk, ])
    data = {
        "code": "text",
        "name": "text",
        "account_type": "text",
        "is_active": True,
        "deleted_at": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ChartOfAccountManager_list_view(client):
    instance1 = test_helpers.create_coreblock_ChartOfAccountManager()
    instance2 = test_helpers.create_coreblock_ChartOfAccountManager()
    url = reverse("coreblock_ChartOfAccountManager_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_ChartOfAccountManager_create_view(client):
    url = reverse("coreblock_ChartOfAccountManager_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ChartOfAccountManager_detail_view(client):
    instance = test_helpers.create_coreblock_ChartOfAccountManager()
    url = reverse("coreblock_ChartOfAccountManager_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_ChartOfAccountManager_update_view(client):
    instance = test_helpers.create_coreblock_ChartOfAccountManager()
    url = reverse("coreblock_ChartOfAccountManager_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Client_list_view(client):
    instance1 = test_helpers.create_coreblock_Client()
    instance2 = test_helpers.create_coreblock_Client()
    url = reverse("coreblock_Client_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Client_create_view(client):
    url = reverse("coreblock_Client_create")
    data = {
        "name": "text",
        "email": "user@tempurl.com",
        "identity_number": "text",
        "registration_number": "text",
        "trust_date": datetime.now(),
        "trust_division": "text",
        "is_trust": True,
        "marital_status": "text",
        "income_ytd": 1.0,
        "expense_ytd": 1.0,
        "trust_balance": 1.0,
        "vat_number": "text",
        "physical_address": "text",
        "postal_address": "text",
        "is_active": True,
        "deleted_at": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Client_detail_view(client):
    instance = test_helpers.create_coreblock_Client()
    url = reverse("coreblock_Client_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Client_update_view(client):
    instance = test_helpers.create_coreblock_Client()
    url = reverse("coreblock_Client_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "email": "user@tempurl.com",
        "identity_number": "text",
        "registration_number": "text",
        "trust_date": datetime.now(),
        "trust_division": "text",
        "is_trust": True,
        "marital_status": "text",
        "income_ytd": 1.0,
        "expense_ytd": 1.0,
        "trust_balance": 1.0,
        "vat_number": "text",
        "physical_address": "text",
        "postal_address": "text",
        "is_active": True,
        "deleted_at": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ClientManager_list_view(client):
    instance1 = test_helpers.create_coreblock_ClientManager()
    instance2 = test_helpers.create_coreblock_ClientManager()
    url = reverse("coreblock_ClientManager_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_ClientManager_create_view(client):
    url = reverse("coreblock_ClientManager_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ClientManager_detail_view(client):
    instance = test_helpers.create_coreblock_ClientManager()
    url = reverse("coreblock_ClientManager_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_ClientManager_update_view(client):
    instance = test_helpers.create_coreblock_ClientManager()
    url = reverse("coreblock_ClientManager_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Creditor_list_view(client):
    instance1 = test_helpers.create_coreblock_Creditor()
    instance2 = test_helpers.create_coreblock_Creditor()
    url = reverse("coreblock_Creditor_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Creditor_create_view(client):
    url = reverse("coreblock_Creditor_create")
    data = {
        "name": "text",
        "amount_owed": 1.0,
        "external_ref": "text",
        "is_active": True,
        "deleted_at": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Creditor_detail_view(client):
    instance = test_helpers.create_coreblock_Creditor()
    url = reverse("coreblock_Creditor_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Creditor_update_view(client):
    instance = test_helpers.create_coreblock_Creditor()
    url = reverse("coreblock_Creditor_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "amount_owed": 1.0,
        "external_ref": "text",
        "is_active": True,
        "deleted_at": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_CreditorManager_list_view(client):
    instance1 = test_helpers.create_coreblock_CreditorManager()
    instance2 = test_helpers.create_coreblock_CreditorManager()
    url = reverse("coreblock_CreditorManager_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_CreditorManager_create_view(client):
    url = reverse("coreblock_CreditorManager_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_CreditorManager_detail_view(client):
    instance = test_helpers.create_coreblock_CreditorManager()
    url = reverse("coreblock_CreditorManager_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_CreditorManager_update_view(client):
    instance = test_helpers.create_coreblock_CreditorManager()
    url = reverse("coreblock_CreditorManager_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Debtor_list_view(client):
    instance1 = test_helpers.create_coreblock_Debtor()
    instance2 = test_helpers.create_coreblock_Debtor()
    url = reverse("coreblock_Debtor_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Debtor_create_view(client):
    url = reverse("coreblock_Debtor_create")
    data = {
        "name": "text",
        "amount_due": 1.0,
        "external_ref": "text",
        "is_active": True,
        "deleted_at": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Debtor_detail_view(client):
    instance = test_helpers.create_coreblock_Debtor()
    url = reverse("coreblock_Debtor_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Debtor_update_view(client):
    instance = test_helpers.create_coreblock_Debtor()
    url = reverse("coreblock_Debtor_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "amount_due": 1.0,
        "external_ref": "text",
        "is_active": True,
        "deleted_at": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_DebtorManager_list_view(client):
    instance1 = test_helpers.create_coreblock_DebtorManager()
    instance2 = test_helpers.create_coreblock_DebtorManager()
    url = reverse("coreblock_DebtorManager_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_DebtorManager_create_view(client):
    url = reverse("coreblock_DebtorManager_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_DebtorManager_detail_view(client):
    instance = test_helpers.create_coreblock_DebtorManager()
    url = reverse("coreblock_DebtorManager_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_DebtorManager_update_view(client):
    instance = test_helpers.create_coreblock_DebtorManager()
    url = reverse("coreblock_DebtorManager_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Employee_list_view(client):
    instance1 = test_helpers.create_coreblock_Employee()
    instance2 = test_helpers.create_coreblock_Employee()
    url = reverse("coreblock_Employee_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Employee_create_view(client):
    url = reverse("coreblock_Employee_create")
    data = {
        "name": "text",
        "email": "user@tempurl.com",
        "is_active": True,
        "deleted_at": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Employee_detail_view(client):
    instance = test_helpers.create_coreblock_Employee()
    url = reverse("coreblock_Employee_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Employee_update_view(client):
    instance = test_helpers.create_coreblock_Employee()
    url = reverse("coreblock_Employee_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "email": "user@tempurl.com",
        "is_active": True,
        "deleted_at": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_EmployeeManager_list_view(client):
    instance1 = test_helpers.create_coreblock_EmployeeManager()
    instance2 = test_helpers.create_coreblock_EmployeeManager()
    url = reverse("coreblock_EmployeeManager_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_EmployeeManager_create_view(client):
    url = reverse("coreblock_EmployeeManager_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_EmployeeManager_detail_view(client):
    instance = test_helpers.create_coreblock_EmployeeManager()
    url = reverse("coreblock_EmployeeManager_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_EmployeeManager_update_view(client):
    instance = test_helpers.create_coreblock_EmployeeManager()
    url = reverse("coreblock_EmployeeManager_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_FinancialTransaction_list_view(client):
    instance1 = test_helpers.create_coreblock_FinancialTransaction()
    instance2 = test_helpers.create_coreblock_FinancialTransaction()
    url = reverse("coreblock_FinancialTransaction_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_FinancialTransaction_create_view(client):
    url = reverse("coreblock_FinancialTransaction_create")
    data = {
        "description": "text",
        "amount": 1.0,
        "transaction_type": "text",
        "transaction_date": datetime.now(),
        "vat_flag": True,
        "is_trust_transaction": True,
        "is_active": True,
        "deleted_at": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_FinancialTransaction_detail_view(client):
    instance = test_helpers.create_coreblock_FinancialTransaction()
    url = reverse("coreblock_FinancialTransaction_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_FinancialTransaction_update_view(client):
    instance = test_helpers.create_coreblock_FinancialTransaction()
    url = reverse("coreblock_FinancialTransaction_update", args=[instance.pk, ])
    data = {
        "description": "text",
        "amount": 1.0,
        "transaction_type": "text",
        "transaction_date": datetime.now(),
        "vat_flag": True,
        "is_trust_transaction": True,
        "is_active": True,
        "deleted_at": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_FinancialTransactionManager_list_view(client):
    instance1 = test_helpers.create_coreblock_FinancialTransactionManager()
    instance2 = test_helpers.create_coreblock_FinancialTransactionManager()
    url = reverse("coreblock_FinancialTransactionManager_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_FinancialTransactionManager_create_view(client):
    url = reverse("coreblock_FinancialTransactionManager_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_FinancialTransactionManager_detail_view(client):
    instance = test_helpers.create_coreblock_FinancialTransactionManager()
    url = reverse("coreblock_FinancialTransactionManager_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_FinancialTransactionManager_update_view(client):
    instance = test_helpers.create_coreblock_FinancialTransactionManager()
    url = reverse("coreblock_FinancialTransactionManager_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Matter_list_view(client):
    instance1 = test_helpers.create_coreblock_Matter()
    instance2 = test_helpers.create_coreblock_Matter()
    url = reverse("coreblock_Matter_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Matter_create_view(client):
    url = reverse("coreblock_Matter_create")
    data = {
        "description": "text",
        "matter_type": "text",
        "status": "text",
        "is_active": True,
        "deleted_at": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Matter_detail_view(client):
    instance = test_helpers.create_coreblock_Matter()
    url = reverse("coreblock_Matter_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Matter_update_view(client):
    instance = test_helpers.create_coreblock_Matter()
    url = reverse("coreblock_Matter_update", args=[instance.pk, ])
    data = {
        "description": "text",
        "matter_type": "text",
        "status": "text",
        "is_active": True,
        "deleted_at": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_MatterManager_list_view(client):
    instance1 = test_helpers.create_coreblock_MatterManager()
    instance2 = test_helpers.create_coreblock_MatterManager()
    url = reverse("coreblock_MatterManager_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_MatterManager_create_view(client):
    url = reverse("coreblock_MatterManager_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_MatterManager_detail_view(client):
    instance = test_helpers.create_coreblock_MatterManager()
    url = reverse("coreblock_MatterManager_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_MatterManager_update_view(client):
    instance = test_helpers.create_coreblock_MatterManager()
    url = reverse("coreblock_MatterManager_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_SystemAccount_list_view(client):
    instance1 = test_helpers.create_coreblock_SystemAccount()
    instance2 = test_helpers.create_coreblock_SystemAccount()
    url = reverse("coreblock_SystemAccount_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_SystemAccount_create_view(client):
    url = reverse("coreblock_SystemAccount_create")
    data = {
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "is_active": True,
        "deleted_at": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_SystemAccount_detail_view(client):
    instance = test_helpers.create_coreblock_SystemAccount()
    url = reverse("coreblock_SystemAccount_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_SystemAccount_update_view(client):
    instance = test_helpers.create_coreblock_SystemAccount()
    url = reverse("coreblock_SystemAccount_update", args=[instance.pk, ])
    data = {
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "is_active": True,
        "deleted_at": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_VatRate_list_view(client):
    instance1 = test_helpers.create_coreblock_VatRate()
    instance2 = test_helpers.create_coreblock_VatRate()
    url = reverse("coreblock_VatRate_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_VatRate_create_view(client):
    url = reverse("coreblock_VatRate_create")
    data = {
        "effective_from": datetime.now(),
        "effective_to": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_VatRate_detail_view(client):
    instance = test_helpers.create_coreblock_VatRate()
    url = reverse("coreblock_VatRate_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_VatRate_update_view(client):
    instance = test_helpers.create_coreblock_VatRate()
    url = reverse("coreblock_VatRate_update", args=[instance.pk, ])
    data = {
        "effective_from": datetime.now(),
        "effective_to": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_VatRateManager_list_view(client):
    instance1 = test_helpers.create_coreblock_VatRateManager()
    instance2 = test_helpers.create_coreblock_VatRateManager()
    url = reverse("coreblock_VatRateManager_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_VatRateManager_create_view(client):
    url = reverse("coreblock_VatRateManager_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_VatRateManager_detail_view(client):
    instance = test_helpers.create_coreblock_VatRateManager()
    url = reverse("coreblock_VatRateManager_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_VatRateManager_update_view(client):
    instance = test_helpers.create_coreblock_VatRateManager()
    url = reverse("coreblock_VatRateManager_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302

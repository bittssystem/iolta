from rest_framework import serializers

from . import models


class ActiveManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ActiveManager
        fields = [
        ]

class ChartOfAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ChartOfAccount
        fields = [
            "code",
            "name",
            "account_type",
            "is_active",
            "deleted_at",
            "created_at",
            "updated_at",
        ]

class ChartOfAccountManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ChartOfAccountManager
        fields = [
        ]

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Client
        fields = [
            "name",
            "email",
            "identity_number",
            "registration_number",
            "trust_date",
            "trust_division",
            "is_trust",
            "marital_status",
            "income_ytd",
            "expense_ytd",
            "trust_balance",
            "vat_number",
            "physical_address",
            "postal_address",
            "is_active",
            "deleted_at",
            "created_at",
            "updated_at",
        ]

class ClientManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ClientManager
        fields = [
        ]

class CreditorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Creditor
        fields = [
            "name",
            "amount_owed",
            "external_ref",
            "is_active",
            "deleted_at",
            "created_at",
            "updated_at",
        ]

class CreditorManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CreditorManager
        fields = [
        ]

class DebtorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Debtor
        fields = [
            "name",
            "amount_due",
            "external_ref",
            "is_active",
            "deleted_at",
            "created_at",
            "updated_at",
        ]

class DebtorManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DebtorManager
        fields = [
        ]

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Employee
        fields = [
            "name",
            "email",
            "is_active",
            "deleted_at",
            "created_at",
            "updated_at",
        ]

class EmployeeManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EmployeeManager
        fields = [
        ]

class FinancialTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FinancialTransaction
        fields = [
            "description",
            "amount",
            "transaction_type",
            "transaction_date",
            "vat_flag",
            "is_trust_transaction",
            "is_active",
            "deleted_at",
            "created_at",
            "updated_at",
        ]

class FinancialTransactionManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FinancialTransactionManager
        fields = [
        ]

class MatterSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Matter
        fields = [
            "description",
            "matter_type",
            "status",
            "is_active",
            "deleted_at",
            "created_at",
            "updated_at",
        ]

class MatterManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MatterManager
        fields = [
        ]

class SystemAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SystemAccount
        fields = [
            "created_at",
            "updated_at",
            "is_active",
            "deleted_at",
        ]

class VatRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.VatRate
        fields = [
            "effective_from",
            "effective_to",
            "created_at",
            "updated_at",
        ]

class VatRateManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.VatRateManager
        fields = [
        ]

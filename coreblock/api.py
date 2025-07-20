from rest_framework import viewsets, permissions

from . import serializers
from . import models


class ActiveManagerViewSet(viewsets.ModelViewSet):
    """ViewSet for the ActiveManager class"""

    queryset = models.ActiveManager.objects.all()
    serializer_class = serializers.ActiveManagerSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChartOfAccountViewSet(viewsets.ModelViewSet):
    """ViewSet for the ChartOfAccount class"""

    queryset = models.ChartOfAccount.objects.all()
    serializer_class = serializers.ChartOfAccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChartOfAccountManagerViewSet(viewsets.ModelViewSet):
    """ViewSet for the ChartOfAccountManager class"""

    queryset = models.ChartOfAccountManager.objects.all()
    serializer_class = serializers.ChartOfAccountManagerSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientViewSet(viewsets.ModelViewSet):
    """ViewSet for the Client class"""

    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientManagerViewSet(viewsets.ModelViewSet):
    """ViewSet for the ClientManager class"""

    queryset = models.ClientManager.objects.all()
    serializer_class = serializers.ClientManagerSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreditorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Creditor class"""

    queryset = models.Creditor.objects.all()
    serializer_class = serializers.CreditorSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreditorManagerViewSet(viewsets.ModelViewSet):
    """ViewSet for the CreditorManager class"""

    queryset = models.CreditorManager.objects.all()
    serializer_class = serializers.CreditorManagerSerializer
    permission_classes = [permissions.IsAuthenticated]


class DebtorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Debtor class"""

    queryset = models.Debtor.objects.all()
    serializer_class = serializers.DebtorSerializer
    permission_classes = [permissions.IsAuthenticated]


class DebtorManagerViewSet(viewsets.ModelViewSet):
    """ViewSet for the DebtorManager class"""

    queryset = models.DebtorManager.objects.all()
    serializer_class = serializers.DebtorManagerSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeViewSet(viewsets.ModelViewSet):
    """ViewSet for the Employee class"""

    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeManagerViewSet(viewsets.ModelViewSet):
    """ViewSet for the EmployeeManager class"""

    queryset = models.EmployeeManager.objects.all()
    serializer_class = serializers.EmployeeManagerSerializer
    permission_classes = [permissions.IsAuthenticated]


class FinancialTransactionViewSet(viewsets.ModelViewSet):
    """ViewSet for the FinancialTransaction class"""

    queryset = models.FinancialTransaction.objects.all()
    serializer_class = serializers.FinancialTransactionSerializer
    permission_classes = [permissions.IsAuthenticated]


class FinancialTransactionManagerViewSet(viewsets.ModelViewSet):
    """ViewSet for the FinancialTransactionManager class"""

    queryset = models.FinancialTransactionManager.objects.all()
    serializer_class = serializers.FinancialTransactionManagerSerializer
    permission_classes = [permissions.IsAuthenticated]


class MatterViewSet(viewsets.ModelViewSet):
    """ViewSet for the Matter class"""

    queryset = models.Matter.objects.all()
    serializer_class = serializers.MatterSerializer
    permission_classes = [permissions.IsAuthenticated]


class MatterManagerViewSet(viewsets.ModelViewSet):
    """ViewSet for the MatterManager class"""

    queryset = models.MatterManager.objects.all()
    serializer_class = serializers.MatterManagerSerializer
    permission_classes = [permissions.IsAuthenticated]


class SystemAccountViewSet(viewsets.ModelViewSet):
    """ViewSet for the SystemAccount class"""

    queryset = models.SystemAccount.objects.all()
    serializer_class = serializers.SystemAccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class VatRateViewSet(viewsets.ModelViewSet):
    """ViewSet for the VatRate class"""

    queryset = models.VatRate.objects.all()
    serializer_class = serializers.VatRateSerializer
    permission_classes = [permissions.IsAuthenticated]


class VatRateManagerViewSet(viewsets.ModelViewSet):
    """ViewSet for the VatRateManager class"""

    queryset = models.VatRateManager.objects.all()
    serializer_class = serializers.VatRateManagerSerializer
    permission_classes = [permissions.IsAuthenticated]

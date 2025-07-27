from rest_framework import viewsets, permissions

from . import serializers
from . import models

# Only import actual models, not managers
from coreblock.models import VatRate, SystemAccount, ChartOfAccount, Client, Employee, Creditor, Debtor, Matter, FinancialTransaction


class ChartOfAccountViewSet(viewsets.ModelViewSet):
    """ViewSet for the ChartOfAccount class"""
    queryset = models.ChartOfAccount.objects.all()
    serializer_class = serializers.ChartOfAccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientViewSet(viewsets.ModelViewSet):
    """ViewSet for the Client class"""
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreditorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Creditor class"""
    queryset = models.Creditor.objects.all()
    serializer_class = serializers.CreditorSerializer
    permission_classes = [permissions.IsAuthenticated]


class DebtorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Debtor class"""
    queryset = models.Debtor.objects.all()
    serializer_class = serializers.DebtorSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeViewSet(viewsets.ModelViewSet):
    """ViewSet for the Employee class"""
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class FinancialTransactionViewSet(viewsets.ModelViewSet):
    """ViewSet for the FinancialTransaction class"""
    queryset = models.FinancialTransaction.objects.all()
    serializer_class = serializers.FinancialTransactionSerializer
    permission_classes = [permissions.IsAuthenticated]


class MatterViewSet(viewsets.ModelViewSet):
    """ViewSet for the Matter class"""
    queryset = models.Matter.objects.all()
    serializer_class = serializers.MatterSerializer
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
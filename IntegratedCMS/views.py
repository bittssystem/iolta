from dal import autocomplete
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ChartOfAccount, Client, Employee, Matter

class ChartOfAccountAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    """Autocomplete view for ChartOfAccount model."""
    def get_queryset(self):
        # Use all_objects to include soft-deleted records
        qs = ChartOfAccount.all_objects.all()
        if self.q:  # Filter based on search query
            qs = qs.filter(name__icontains=self.q) | qs.filter(code__icontains=self.q)
        return qs

class ClientAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    """Autocomplete view for Client model."""
    def get_queryset(self):
        qs = Client.all_objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q) | qs.filter(email__icontains=self.q)
        return qs

class EmployeeAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    """Autocomplete view for Employee model."""
    def get_queryset(self):
        qs = Employee.all_objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q) | qs.filter(email__icontains=self.q)
        return qs

class MatterAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    """Autocomplete view for Matter model."""
    def get_queryset(self):
        qs = Matter.all_objects.all()
        if self.q:
            qs = qs.filter(description__icontains=self.q) | qs.filter(client__name__icontains=self.q)
        return qs
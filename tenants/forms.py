from django import forms
from .models import Tenant, Invoice

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'email', 'phone_number']


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['tenant', 'amount', 'due_date', 'is_paid']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }
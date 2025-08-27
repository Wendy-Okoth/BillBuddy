from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 
from .forms import TenantForm, InvoiceForm
from .models import Tenant, Invoice

@login_required
def add_tenant(request):
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tenants')
    else:
        form = TenantForm()
    
    return render(request, 'tenants/add_tenant.html', {'form': form})

@login_required
def list_tenants(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenants/list_tenants.html', {'tenants': tenants})

@login_required
def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tenants')
    else:
        form = InvoiceForm()
        
    return render(request, 'tenants/create_invoice.html', {'form': form})

@login_required
def list_invoices(request):
    invoices = Invoice.objects.all()
    return render(request, 'tenants/list_invoices.html', {'invoices': invoices})

@login_required
def tenant_invoices(request):
    try:
        # Get the tenant record linked to the logged-in user
        tenant = request.user.tenant
        
        # Filter invoices that belong to that specific tenant
        invoices = Invoice.objects.filter(tenant=tenant)
        
    except Tenant.DoesNotExist:
        invoices = None
    
    return render(request, 'tenants/tenant_invoices.html', {'invoices': invoices})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        tenant_form = TenantForm(request.POST)
        if form.is_valid() and tenant_form.is_valid():
            user = form.save()
            tenant = tenant_form.save(commit=False)
            tenant.user = user  # Link the user to the tenant
            tenant.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        tenant_form = TenantForm()
    
    return render(request, 'registration/signup.html', {
        'form': form,
        'tenant_form': tenant_form
    })
# Create your views here.

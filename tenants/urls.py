from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # <-- Fix the yellow line here

urlpatterns = [
    path('add/', views.add_tenant, name='add_tenant'),
    path('', views.list_tenants, name='list_tenants'),
    path('invoice/create/', views.create_invoice, name='create_invoice'),
    path('invoice/', views.list_invoices, name='list_invoices'),

    # User Authentication URLs
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    # Tenant-side portal URL
    path('dashboard/', views.tenant_invoices, name='tenant_invoices'),

    path('signup/', views.signup, name='signup'), 
]
from django.db import models
from django.conf import settings

class Tenant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Invoice(models.Model):
    # This is a link to the Tenant model
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    
    # Invoice details
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Invoice for {self.tenant.name} - ${self.amount}"
    
# Create your models here.

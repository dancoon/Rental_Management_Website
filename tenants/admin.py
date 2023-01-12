from django.contrib import admin
from .models import Tenant, PaymentStatement, TenantFeedback

# Register your models here.
@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ['phone']

@admin.register(PaymentStatement)
class PaymentStatementAdmin(admin.ModelAdmin):
    list_display = ['tenant_name', 'amount', 'date', 'payment_for']

@admin.register(TenantFeedback)
class TenantFeedbackAdmin(admin.ModelAdmin):
    list_display = ['tenant_name', 'feedback']
    
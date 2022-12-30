from django.contrib import admin
from .models import Tenant, Contact, Owner, Announcements, Applicant, Room, Payment, TenantFeedback, PaymentStatement

# Register your models here.
@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email']
    search_fields = ['first_name']

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    pass

@admin.register(Announcements)
class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ['sender', 'to', 'message', 'type', 'date']

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room', 'type', 'occupied']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['tenant', 'amount', 'date', 'payment_for']

@admin.register(PaymentStatement)
class PaymentStatementAdmin(admin.ModelAdmin):
    list_display = ['tenant_name', 'amount', 'date', 'payment_for']

@admin.register(TenantFeedback)
class TenantFeedbackAdmin(admin.ModelAdmin):
    list_display = ['tenant_name', 'feedback']
    
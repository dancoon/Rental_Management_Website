from django.contrib import admin
from .models import Contact, Owner, Announcements, Room, Payment

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'comment']

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    pass

@admin.register(Announcements)
class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ['sender', 'to', 'message', 'type', 'date']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room', 'type', 'occupied']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['tenant', 'amount', 'date', 'payment_for']

from django.contrib import admin
from .models import  Applicant

# Register your models here.
@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'phone', 'id_number', 'room_type', 'gender']
    

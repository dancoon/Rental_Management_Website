from django.shortcuts import render, redirect, reverse
from .models import Contact, Announcements, Payment, Room
from core.models import Applicant
from tenants.models import Tenant, PaymentStatement, TenantFeedback
from tenants.views import is_tenant
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required,user_passes_test
from django.utils.timezone import datetime
from django.utils import timezone
from django.contrib import messages

# Create your views here.
def display_admin_account(request):
    applicants = Applicant.objects.all().count()
    month = datetime.now().strftime("%B")
    payments = Payment.objects.filter(payment_for=month).count()
    comments = Contact.objects.all().count()
    rooms = Room.objects.filter(occupied=True).count()
    context = {
        'applicants': applicants,
        'payments': payments,
        'month': month,
        'comments': comments,
        'rooms': rooms,
    }
    return render(request, 'components/owner.html', context=context)

def owner_tenants_info(request):
    applicant = Applicant.objects.all()
    tenant = Tenant.objects.filter(status=True)
    # clearing_tenants =
    context = {
     'applicant': applicant,
     'tenant': tenant,
    }
    return render(request, 'components/tenantsinfo.html', context=context)

def owner_rooms_info(request):
    vacant = Room.objects.all()
    context = {
     'vacant': vacant,
    }
    return render(request, 'components/roomsinfo.html', context=context)

def enroll_tenants(request, pk):
    applicant = Applicant.objects.get(id=pk)
    rm = Room.objects.filter(occupied=False, type=applicant.room_type).first()
    house = Room.objects.get(id=rm.id)
    user = User.objects.get(username=applicant.first_name)
    new = Tenant(user=user, gender = applicant.gender, phone = applicant.phone, id_number=applicant.id_number, status = True, room_id = rm.id)
    new.save()
    house.occupied = True
    house.save()
    applicant.delete()
    return redirect(reverse('enroll_tenants_view'))         

def enroll_tenants_view(request):
    applicants = Applicant.objects.all()
    context = {
        'applicants': applicants,
    }
    return render(request, 'components/enroll.html', context=context)

def view_tenants_pay(request):
    pay_statement = PaymentStatement.objects.all()
    confirmed_pay = Payment.objects.all()
    context = {
        'payment_statement': pay_statement,
        'confirmed_pay': confirmed_pay,
    }
    return render(request, 'components/rents.html', context=context)

def view_comments(request):
    contact = Contact.objects.all()
    context = {
        'comment': contact,
    }
    return render(request, 'components/comments.html', context)
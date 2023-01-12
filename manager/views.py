from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .forms import ApplicationForm
from .models import Contact, Announcements, Applicant, Payment, Room, PaymentStatement, TenantFeedback
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
    payments = 1
    comments = Contact.objects.all().count()
    rooms = Room.objects.filter(occupied=True).count()
    context = {
        'applicants': applicants,
        'payments': payments,
        'month': month,
        'comments': comments,
        'rooms': rooms,
    }
    return render(request, 'signed/owner/owner.html', context=context)

def owner_tenants_info(request):
    applicant = Applicant.objects.all()
    tenant = Tenant.objects.all().filter(status=True)
    context = {
     'applicant': applicant,
     'tenant': tenant,
    }
    return render(request, 'signed/owner/tenantsinfo.html', context=context)

def owner_rooms_info(request):
    vacant = Room.objects.all()
    context = {
     'vacant': vacant,
    }
    return render(request, 'signed/owner/roomsinfo.html', context=context)

def enroll_tenants(request, pk):
    app = Applicant.objects.get(id=pk)
    applicants = Applicant.objects.all()
    rm = app.room_type
    print(rm) 
    rm = Room.objects.filter(occupied=False, type='bedsitter').first()
    room = rm.id
    house = Room.objects.get(id=room)
    house.occupied = True
    house.save()
    user = User.objects.get(username=app.first_name)
    new = Tenant()
    new.user = user
    new.first_name = app.first_name
    new.last_name = app.last_name
    new.gender = 'male'
    new.phone = app.phone
    new.email = app.email
    new.id_number = app.id_number
    new.status = True
    new.room_id = room
    new.save()
    app.delete()
    context = {
        'applicants': applicants,
    }
    return redirect(reverse('enroll_tenants_view'))         

def enroll_tenants_view(request):
    applicants = Applicant.objects.all()
    context = {
        'applicants': applicants,
    }
    return render(request, 'signed/owner/enroll.html', context=context)

def view_tenants_pay(request):
    pay_statement = PaymentStatement.objects.all()
    confirmed_pay = Payment.objects.all()
    context = {
        'payment_statement': pay_statement,
        'confirmed_pay': confirmed_pay,
    }
    return render(request, 'signed/owner/rents.html', context=context)

def view_comments(request):
    contact = Contact.objects.all()
    context = {
        'comment': contact,
    }
    return render(request, 'signed/owner/comments.html', context)
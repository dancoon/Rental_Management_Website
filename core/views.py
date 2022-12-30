from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ApplicationForm
from .models import Contact, Tenant, Announcements, Applicant, Payment, Room
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required,user_passes_test
from django.utils.timezone import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        obj = Contact(name=name, email=email, comment=comment)
        obj.save()
        return HttpResponse("Data saved")
    else:
        return render(request, 'index.html')

#users sign in
def signin(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        user = authenticate(request, username=name, email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, "Log in success")
            return redirect('/tenant/')
        else:
            return redirect('/')
    else:
        return render(request, 'signin.html')

# def logout(request):
#     logout(request)
#     messages.info(request, "Log out success")
#     return redirect('/')

#users sign up
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        user = User(username=name, email=email, password=password)
        user.set_password(password)
        user.save()

        my_tenant_group = Group.objects.get(name='TENANT')
        user.groups.add(my_tenant_group)
        messages.success(request, "Sign up complete")
        return redirect('/application/')
    else:        
        return render(request, 'signup.html')

def apply_tenancy(request):
    form = ApplicationForm()
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            first_name = cd.get("first_name")
            last_name = cd.get("last_name")
            gender = cd.get("username")
            e = cd.get("email")
            phone = cd.get("phone")
            id_number = cd.get("id_number")

            applicant = Applicant(first_name=first_name,last_name=last_name,gender=gender,email=e,phone=phone,id_number=id_number)        
            applicant.save()

            return redirect('/signin/')
    context = {
        'form': form,
            }
    return render(request, 'application.html', context)
    
#check role of the user
def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_tenant(user):
    return user.groups.filter(name='TENANT').exists()
def is_owner(user):
    return user.groups.filter(name='OWNER').exists()

#tenants behaviour
@login_required
@user_passes_test(is_tenant)
def display_tenant_account(request):
    if is_tenant(request.user):
        tenantapproval = Tenant.objects.all().filter(user_id=request.user.id, status=True)
        if tenantapproval:
            tenant = Tenant.objects.all().filter(status=True, user_id=request.user.id).first()
            
            mes = None
            if Announcements.objects.all().filter(to='all').count() > 0:
                mes = Announcements.objects.all().filter(date=datetime.today())

            amount = 0
            balance = 0
            if Payment.objects.all().filter(tenant_id=request.user.id):
                receipt = Payment.objects.all().filter(tenant_id=request.user.id).last()
                amount = receipt.amount
                balance = receipt.rent_to_be_paid(tenant.room)
                paymentfor = receipt.payment_for
            context = {
                'tenant_name': tenant.first_name,
                'message_notification': mes,
                'amount': amount,
                'room_no': tenant.room,
                'balance': balance,
                'months_stayed': paymentfor,
            }
            return render(request, 'signed/tenant/tenant.html', context=context)
        else:
            return render(request, 'signed/tenant/tenantwaitforapproval.html')
    else:
        return render(request, 'index.html')


#tenant to post comments and complains
@login_required
@user_passes_test(is_tenant)
def tenant_comment(request):
    if is_tenant(request.user):
        tenantapproval = Tenant.objects.all().filter(user_id=request.user.id, status=True)
        if tenantapproval:
            tenant = Tenant.objects.all().filter(status=True, user_id=request.user.id)
            message_notification = None
            if Announcements.objects.all().filter(to='all').count() > 0:
                today = datetime.today()
                message_notification = Announcements.objects.all().filter(date=today)
            
            context = {
                'tenant_name': tenant[0].first_name,
                'message_notification': message_notification,
            }
        return render(request, 'signed/tenant/comments.html', context=context)


#to display announcements and other info to tenants
@login_required
@user_passes_test(is_tenant)
def tenant_info(request):
    if is_tenant(request.user):
        tenantapproval = Tenant.objects.all().filter(user_id=request.user.id, status=True)
        if tenantapproval:
            tenant = Tenant.objects.all().filter(status=True, user_id=request.user.id)
            message_notification = None
            message = None
            if Announcements.objects.all().count() > 0:
                message = Announcements.objects.all()
                today = datetime.today()
                message_notification = Announcements.objects.all().filter(date=today)

            context = {
                'tenant_name': tenant[0].first_name,
                'message': message,
                'message_notification': message_notification,
            }
        return render(request, 'signed/tenant/info.html', context)


#to display payment receipts for tenants
@login_required
@user_passes_test(is_tenant)
def tenant_rent(request):
    if is_tenant(request.user):
        tenantapproval = Tenant.objects.all().filter(user_id=request.user.id, status=True)
        if tenantapproval:
            tenant = Tenant.objects.all().filter(status=True, user_id=request.user.id)
            message_notification = None
            if Announcements.objects.all().filter(to='all').count() > 0:
                today = datetime.today()
                message_notification = Announcements.objects.all().filter(date=today)
            
            receipt = None
            if Payment.objects.all().filter(tenant_id=request.user.id):
                receipt = Payment.objects.all().filter(tenant_id=request.user.id)
            context = {
                'tenant_name': tenant[0].first_name,
                'message_notification': message_notification,
                'receipt': receipt
            }
        return render(request, 'signed/tenant/rent.html', context=context)


#tenant to confirm their payment for rent
@login_required
@user_passes_test(is_tenant)
def tenant_payment(request):
    if is_tenant(request.user):
        tenantapproval = Tenant.objects.all().filter(user_id=request.user.id, status=True)
        if tenantapproval:
            tenant = Tenant.objects.all().filter(status=True, user_id=request.user.id)
            message_notification = None
            if Announcements.objects.all().filter(to='all').count() > 0:
                today = datetime.today()
                message_notification = Announcements.objects.all().filter(date=today)
                
            context = {
                'tenant_name': tenant[0].first_name,
                'message_notification': message_notification,
            }
        return render(request, 'signed/tenant/payments.html', context=context)

from django.shortcuts import render
from django.http import HttpResponse
from .models import Tenant
from manager.models import Payment, Announcements, PaymentStatement
from django.contrib.auth.decorators import login_required,user_passes_test
from django.utils.timezone import datetime
from django.contrib.auth.models import User

# Create your views here.
def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_tenant(user):
    return user.groups.filter(name='TENANT').exists()
def is_owner(user):
    return user.groups.filter(name='OWNER').exists()
    
@login_required
@user_passes_test(is_tenant)
def display_tenant_account(request):
    if is_tenant(request.user):
        tenantapproval = Tenant.objects.filter(user_id=request.user.id, status=True)
        if tenantapproval:
            tenant = Tenant.objects.get(status=True, user_id=request.user.id)
            
            mes = None
            if Announcements.objects.filter(to='all').count():
                today = datetime.today()
                mes = Announcements.objects.filter(date=today)

            stay = None
            amount = 0
            balance = 0
            if Payment.objects.filter(tenant_id=request.user.id):
                receipt = Payment.objects.filter(tenant_id=request.user.id).first()
                amount = receipt.amount
                balance = receipt.balance

            context = {
                'tenant_name': tenant.get_name,
                'message_notification': mes,
                'amount': amount,
                'room_no': tenant.room,
                'balance': balance,
                'months_stayed': stay,
            }
            return render(request, 'tenant/tenant.html', context=context)
        else:
            return HttpResponse("Wait for approval")
    else:
        return render(request, 'index.html')

#tenant to post comments and complains
@login_required
@user_passes_test(is_tenant)
def tenant_comment(request):
    if is_tenant(request.user):
        tenantapproval = Tenant.objects.filter(user_id=request.user.id, status=True)
        if tenantapproval:
            tenant = Tenant.objects.filter(status=True, user_id=request.user.id)
            message_notification = None
            if Announcements.objects.filter(to='all').count() > 0:
                today = datetime.today()
                message_notification = Announcements.objects.filter(date=today)
            
            context = {
                'tenant_name': tenant[0].get_name,
                'message_notification': message_notification,
            }
        return render(request, 'tenant/comments.html', context=context)

#to display announcements and other info to tenants
@login_required
@user_passes_test(is_tenant)
def tenant_info(request):
    if is_tenant(request.user):
        tenantapproval = Tenant.objects.filter(user_id=request.user.id, status=True)
        if tenantapproval:
            tenant = Tenant.objects.filter(status=True, user_id=request.user.id)
            message_notification = None
            message = None
            if Announcements.objects.all().count() > 0:
                message = Announcements.objects.all()
                today = datetime.today()
                message_notification = Announcements.objects.filter(date=today)

            context = {
                'tenant_name': tenant[0].get_name,
                'message': message,
                'message_notification': message_notification,
            }
        return render(request, 'tenant/info.html', context)

#to display payment receipts for tenants
@login_required
@user_passes_test(is_tenant)
def tenant_rent(request):
    if is_tenant(request.user):
        tenantapproval = Tenant.objects.filter(user_id=request.user.id, status=True)
        if tenantapproval:
            tenant = Tenant.objects.filter(status=True, user_id=request.user.id)
            message_notification = None
            if Announcements.objects.filter(to='all').count() > 0:
                today = datetime.today()
                message_notification = Announcements.objects.filter(date=today)
            
            receipt = None
            if Payment.objects.filter(tenant_id=request.user.id):
                receipt = Payment.objects.filter(tenant_id=request.user.id)
            context = {
                'tenant_name': tenant[0].get_name,
                'message_notification': message_notification,
                'receipt': receipt
            }
        return render(request, 'tenant/rent.html', context=context)


#tenant to confirm their payment for rent
@login_required
@user_passes_test(is_tenant)
def tenant_payment(request):
    if is_tenant(request.user):
        tenantapproval = Tenant.objects.filter(user_id=request.user.id, status=True)
        if tenantapproval:
            tenant = Tenant.objects.filter(status=True, user_id=request.user.id)
            message_notification = None
            if request.method == 'POST':
                tenant_name = request.POST['tenant_name']
                mode_of_payment = request.POST['mode_of_payment']
                amount = request.POST['amount']
                payment_for = request.POST['payment_for']
                obj = PaymentStatement(tenant_name=tenant_name, mode_of_payment=mode_of_payment, amount=amount, payment_for=payment_for)
                obj.save()
            if Announcements.objects.filter(to='all'):
                message_notification = Announcements.objects.filter(date=datetime.today())
                
            context = {
                'tenant_name': tenant[0].get_name,
                'message_notification': message_notification,
            }
        return render(request, 'tenant/payments.html', context=context)

from django.shortcuts import render
from .models import Tenant, PaymentStatement, TenantFeedback
from manager.models import Payment, Announcements
from django.contrib.auth.decorators import login_required,user_passes_test
from django.utils.timezone import datetime

today = datetime.today()
def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

def is_tenant(user):
    return user.groups.filter(name='TENANT').exists()

def is_active_tenant(user):
    return Tenant.objects.filter(user_id=user.id, status=True).exists()

def is_owner(user):
    return user.groups.filter(name='OWNER').exists()

def today_announcement():
    mes = None
    if Announcements.objects.filter(to='all').exists():
        mes = Announcements.objects.filter(date=today)
    return mes
    
@login_required
@user_passes_test(is_active_tenant)
def display_tenant_account(request):
    try:
        tenant = Tenant.objects.get(status=True, user_id=request.user.id)
    except Tenant.DoesNotExist:
        tenant = None
    mes = today_announcement()
    stay = None
    amount = 0
    balance = 0
    if Payment.objects.filter(tenant_id=request.user.id).exists():
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

#tenant to post comments and complains
@login_required
@user_passes_test(is_active_tenant)
def tenant_comment(request):
    try:
        tenant = Tenant.objects.get(status=True, user_id=request.user.id)
    except Tenant.DoesNotExist:
        tenant = None
    message_notification = today_announcement()
    if request.method == 'POST':
        tenant_name = request.POST['tenant_name']
        feedback = request.POST['feedback']
        obj = TenantFeedback(tenant_name=tenant_name, feedback=feedback)
        obj.save()
    context = {
        'tenant_name': tenant.get_name,
        'message_notification': message_notification,
    }
    return render(request, 'tenant/comments.html', context=context)

#to display announcements and other info to tenants
@login_required
@user_passes_test(is_active_tenant)
def tenant_info(request):
    message_notification = today_announcement()
    try:
        tenant = Tenant.objects.get(status=True, user_id=request.user.id)
    except Tenant.DoesNotExist:
        tenant = None
    try:
        message = Announcements.objects.all()
    except Announcements.DoesNotExist:
        message = None
    context = {
        'tenant_name': tenant.get_name,
        'message': message,
        'message_notification': message_notification,
    }
    return render(request, 'tenant/info.html', context)

#to display payment receipts for tenants
@login_required
@user_passes_test(is_active_tenant)
def tenant_rent(request):
    message_notification = today_announcement()            
    try:
        tenant = Tenant.objects.get(status=True, user_id=request.user.id)
    except Tenant.DoesNotExist:
        tenant = None
    try:
        receipt = Payment.objects.filter(tenant_id=request.user.id)
    except Payment.DoesNotExist:
        receipt = None
    context = {
        'tenant_name': tenant.get_name,
        'message_notification': message_notification,
        'receipt': receipt
    }
    return render(request, 'tenant/rent.html', context=context)

#tenant to confirm their payment for rent
@login_required
@user_passes_test(is_active_tenant)
def tenant_payment(request):
    message_notification = today_announcement()
    try:
        tenant = Tenant.objects.get(status=True, user_id=request.user.id)
    except Tenant.DoesNotExist:
        tenant = None
    if request.method == 'POST':
        tenant_name = request.POST['tenant_name']
        mode_of_payment = request.POST['mode_of_payment']
        amount = request.POST['amount']
        payment_for = request.POST['payment_for']
        obj = PaymentStatement(tenant_name=tenant_name, mode_of_payment=mode_of_payment, amount=amount, payment_for=payment_for)
        obj.save()            
    context = {
        'tenant_name': tenant.get_name,
        'message_notification': message_notification,
    }
    return render(request, 'tenant/payments.html', context=context)

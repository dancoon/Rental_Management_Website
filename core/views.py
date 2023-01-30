from django.shortcuts import render, redirect, reverse
from .forms import ApplicationForm
from manager.models import Contact, Room
from .models import Applicant
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        obj = Contact(name=name, email=email, comment=comment)
        obj.save()
        return redirect(reverse('index'))
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
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['pass']
        re_pass = request.POST['re_pass']
        if password != re_pass:
            messages.error(request, "Password and Confirm Password do not match!!!")
            return render(request, 'signup.html')
        user = User(username=name, first_name=first_name, last_name=last_name, email=email, password=password)
        user.set_password(password)
        user.save()
        group, created = Group.objects.get_or_create(name='TENANT')
        user.groups.add(group.id)
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
            phone = cd.get("phone")
            id_number = cd.get("id_number")
            room_type = cd.get("room_type")
            applicant = Applicant(first_name=first_name, phone=phone,id_number=id_number,room_type=room_type)        
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

def vacant_room():
    room = Room.objects.all().filter(occupied=False)
    return room

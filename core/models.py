from django.db import models
from django.contrib.auth.models import User, Group

TYPE_CHOICE = (
    ('bedsitter', 'bedsitter'),
    ('single', 'single'),
    ('1 bedroom', '1 bedroom'),
    ('2 bedroom', '2 bedroom'),
    )

GENDER = (
    ('male', 'male'),
    ('female', 'female'),
    ('I prefer not to say', 'I prefer not to say'),
)

SENDER = (
    ('landlord', 'landlord'),
    ('landlady', 'landlady'),
    ('caretaker', 'caretaker'),
)

MESS = (
    ('alert-success', 'alert-success'),
    ('alert-info', 'alert-info'),
    ('alert-warning', 'alert-warning'),
    ('alert-danger', 'alert-danger'),
)

# Create your models here.
class Room(models.Model):
    room = models.CharField(max_length=50)
    type = models.CharField(max_length=200, choices=TYPE_CHOICE)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.room

class Tenant(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=200, choices=GENDER, default='I prefer not to say')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    id_number = models.CharField(max_length=50)
    joined_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    room = models.OneToOneField(Room,on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

class Applicant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    id_number = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Owner(models.Model):
    pass

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    comment = models.TextField()

class Payment(models.Model):
    tenant = models.OneToOneField(Tenant, on_delete=models.CASCADE)
    mode = models.CharField(max_length=50)
    amount = models.PositiveBigIntegerField()
    payment_for = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.tenant + " " + self.amount

class Announcements(models.Model):
    sender = models.CharField(max_length=200, choices=SENDER)
    type = models.CharField(max_length=200, choices=MESS)
    to  = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    message = models.TextField()
    
    @property
    def get_receiver(self):
        return self.to
        
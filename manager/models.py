from django.db import models
from django.contrib.auth.models import User, Group
from django.utils.timezone import datetime
from django.utils import timezone

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

SINGLES_RENT = 3500
BEDSITTER_RENT = 6500
ONEBEDROOM_RENT = 8500
TWOBEDROOM_RENT = 12500


# Create your models here.
class Room(models.Model):
    room = models.CharField(max_length=50)
    type = models.CharField(max_length=200, choices=TYPE_CHOICE)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.room

class Owner(models.Model):
    pass

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    comment = models.TextField()

#approved payments
class Payment(models.Model):
    tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    mode = models.CharField(max_length=50)
    amount = models.PositiveBigIntegerField()
    balance = models.PositiveBigIntegerField(default=0)
    payment_for = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)
    
    @property
    def month_paid(self):
        return self.date.month - timezone.now().month

    def tenant_balance(self, room_no):
        room = Room.objects.all().filter(room=room_no).last()
        if room.type == 'bedsitter':
            rent = BEDSITTER_RENT
        elif room.type == 'single':
            rent = SINGLES_RENT
        elif room.type == '1 bedroom':
            rent = ONEBEDROOM_RENT
        elif room.type == '2 bedroom':
            rent = TWOBEDROOM_RENT
        else:
            rent = -1

        return rent - self.amount

    def set_balance(self, balance):
        self.balance = balance

    # def set_balance(self):
        # self.balance = self.amount
    
    def tenant_balance(self, room_no):
        room = Room.objects.all().filter(room=room_no).last()
        if room.type == 'bedsitter':
            rent = BEDSITTER_RENT
        elif room.type == 'single':
            rent = SINGLES_RENT
        elif room.type == '1 bedroom':
            rent = ONEBEDROOM_RENT
        elif room.type == '2 bedroom':
            rent = TWOBEDROOM_RENT
        else:
            rent = -1

        return rent - self.amount

    def set_balance(self, balance):
        self.balance = balance

    # def set_balance(self):
        # self.balance = self.amount
    
class Announcements(models.Model):
    sender = models.CharField(max_length=200, choices=SENDER)
    type = models.CharField(max_length=200, choices=MESS)
    to  = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    message = models.TextField()
    
    #soon we'll upgrade so that admin can send to people specific
    @property
    def get_receiver(self):
        return self.to

#tenant statement of payment        
class PaymentStatement(models.Model):
    tenant_name = models.CharField(max_length=250)
    mode_of_payment = models.CharField(max_length=50)
    amount = models.PositiveBigIntegerField()
    payment_for = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)

class TenantFeedback(models.Model):
    tenant_name = models.CharField(max_length=250)
    feedback = models.TextField()
    date = models.DateField(auto_now=True)

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from core.models import Room

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
    room = models.ForeignKey(Room,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    
    def get_room(self):
        return self.room

    def months_stayed(self):
        start = self.joined_date
        end = datetime.today()
        months = (end.year - start.year) * 12 + (end.month - start.month)
        return months
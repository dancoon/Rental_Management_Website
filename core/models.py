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
class Applicant(models.Model):
    first_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    id_number = models.CharField(max_length=50)
    room_type = models.CharField(max_length=200, choices=TYPE_CHOICE)

    def __str__(self):
        return self.first_name

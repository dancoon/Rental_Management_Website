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

GENDER_CHOICE = (
    ('male', 'male'),
    ('female', 'female'),
    ('none', 'none'),
)

# Create your models here.
class Applicant(models.Model):
    first_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=200,default='None', choices=GENDER_CHOICE)
    id_number = models.CharField(max_length=50)
    room_type = models.CharField(max_length=200, choices=TYPE_CHOICE)

    def __str__(self):
        return self.first_name
    
  
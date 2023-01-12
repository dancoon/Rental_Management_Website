from django import forms

class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=250)
    phone = forms.CharField(max_length= 250)
    id_number = forms.CharField(max_length=50)
    room_type = forms.CharField(max_length=50)
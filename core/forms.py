from django import forms

class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length= 250)
    last_name = forms.CharField(max_length= 250)
    gender = forms.CharField(max_length= 250)
    email = forms.EmailField()
    phone = forms.CharField(max_length= 250)
    id_number = forms.CharField(max_length=50)

from django import forms
from .models import ChargePointExtra,Client,Users
from django.contrib.auth.models import User
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class ChargePointForm(forms.ModelForm):
    class Meta:
        model = ChargePointExtra
        fields = ['serial', 'model', 'station', 'joindate']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['identifiant_bancaire', 'station', 'type_of_vehicle', 'joindate', 'montant','energy'] 

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['email', 'first_name', 'last_name', 'functions'] 
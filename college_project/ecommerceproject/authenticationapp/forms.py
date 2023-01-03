from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


# class Customer(forms.Form):
#     First_name=forms.CharField()
#     Last_name=forms.CharField()
#     Email_id=forms.EmailField()


class Register(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]
        labels={'password1':'password kro confirm'}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'})
        }
    

class customer(forms.ModelForm):
    class Meta:
        model=Customer
        fields=["First_name","last_name","Email_id","address","land_mark","State","City","pin_code","Mobile_no"]


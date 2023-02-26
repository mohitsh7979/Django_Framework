from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class Myuserform(UserCreationForm):

    class Meta:
        model=User
        fields=["username","first_name","last_name","email"]
        widgets={
            'username':forms.TextInput(attrs={'class':'mohit'})
        }

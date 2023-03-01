from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class usercreationforms(UserCreationForm):

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']


class myform(forms.Form):
    name=forms.CharField()
    age=forms.CharField()


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class details(forms.Form):
    name=forms.CharField()
    skill=forms.CharField()
    address=forms.CharField()
    work_experience=forms.CharField()
    projects=forms.CharField()
    certificates=forms.CharField()
    language=forms.CharField()
    mobile=forms.CharField()
    dob=forms.DateField()
    objective=forms.CharField()
    Email_id=forms.EmailField()
  


class myuser(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']



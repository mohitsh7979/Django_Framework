from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Auth(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confrim Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {

            "username": forms.TextInput(attrs={'placeholder': 'Enter your Username'}),
            "email": forms.TextInput(attrs={'placeholder': 'Enter your email'}),

        }

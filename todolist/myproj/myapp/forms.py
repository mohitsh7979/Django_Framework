from django import forms

class listforms(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    course=forms.CharField()


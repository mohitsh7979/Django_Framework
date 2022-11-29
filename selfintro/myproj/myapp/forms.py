from django import forms

class details(forms.Form):
    name=forms.CharField()
    skill=forms.CharField()
    address=forms.CharField()
    work_experience=forms.CharField()
    projects=forms.CharField()
    certificates=forms.CharField()
    language=forms.CharField()
    intrests=forms.CharField()
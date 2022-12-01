from django import forms

class details(forms.Form):
    name=forms.CharField()
    fname=forms.CharField()
    skill=forms.CharField()
    address=forms.CharField()
    work_experience=forms.CharField()
    projects=forms.CharField()
    certificates=forms.CharField()
    language=forms.CharField()
    intrests=forms.CharField()
    mobile=forms.CharField()
    dob=forms.DateField()
    objective=forms.CharField()
    Email_id=forms.EmailField()

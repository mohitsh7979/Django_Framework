from django import forms

class listforms(forms.Form):
    name=forms.CharField()
    roll_no=forms.IntegerField()
    father_name=forms.CharField()
    date=forms.DateTimeField()
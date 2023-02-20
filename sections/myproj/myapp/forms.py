from django import forms

class listforms(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'m'}))
    roll_no=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    father_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    date=forms.DateTimeField(widget=forms.TextInput(attrs={'class':'form-control'}))
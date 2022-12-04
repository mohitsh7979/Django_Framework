from django import forms
from .models import resume

GENDER_CHOICE=(
    ('Male','Male'),
    ('Female','Female')
)

JOB_CITY_CHOICE=(
    ('Mumbai','Mumbai'),
    ('Pune','Pune'),
    ('Kolkata','Kolkata')
)

class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICE,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(label='Prefered location', choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=resume
        fields=['name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_file']
        labels={'name':'Full Name','dob':'Date of Birth','pin':'Pin code','email':'Email id'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
        }
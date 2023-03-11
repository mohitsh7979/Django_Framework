from django import forms
from .models import Distributer

class DealerForm(forms.Form):
    Business_Name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Mobile_No=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Whatsapp_No=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    District=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Pin_code=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Gst_No=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Seed_License=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))


class DistributerForm(forms.ModelForm):

    class Meta:
        model=Distributer
        print("this is id ",Distributer.id)
       
        fields=["user","Business_Name","Mobile_No","Whatsapp_No","Address","District","Pin_code","Gst_No","Seed_License"]
        widgets={

            'user':forms.Select(attrs={'class':'form-select','aria-label':'Default select example'}),
            'Business_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Mobile_No':forms.TextInput(attrs={'class':'form-control'}),
            'Whatsapp_No':forms.TextInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),
            'District':forms.TextInput(attrs={'class':'form-control'}),
            'Pin_code':forms.TextInput(attrs={'class':'form-control'}),
            'Gst_No':forms.TextInput(attrs={'class':'form-control'}),
            'Seed_License':forms.TextInput(attrs={'class':'form-control'}),
        }

    


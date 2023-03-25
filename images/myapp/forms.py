from django import forms   
from .models import image_upload

class imageforms(forms.ModelForm):
    class Meta:
        model = image_upload
        fields = ["id" , "pan_card" , "aadhar_card"]
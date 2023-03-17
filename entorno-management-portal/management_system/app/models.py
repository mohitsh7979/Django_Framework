from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1, 'admin'),
        (2, 'manager'),
        (3, 'employee'),

    )
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')

class Employee(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='media/profile_pic')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile_no = models.IntegerField(null=True , blank=True)
    gender = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    username =models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.TextField()
    pan_card = models.ImageField(upload_to='media/pan_card')
    adhar_card = models.ImageField(upload_to='media/adhar_card')
    cheque = models.ImageField(upload_to='media/bank_details')   
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.username
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Resume(models.Model):
    
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=100)
    fname=models.CharField(max_length=100)
    Dob=models.DateField()
    mobile_no=models.CharField(max_length=100)
    email=models.EmailField()
    objective=models.CharField(max_length=1000)
    skill=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    work_experience=models.CharField(max_length=100)
    projects=models.CharField(max_length=100)
    certificates=models.CharField(max_length=100)
    language=models.CharField(max_length=100)
    intrests=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media')


# class likes(Resume):
#     like=models.IntegerField()



class likes(Resume):
    myuser=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,parent_link=True)
    like=models.IntegerField()


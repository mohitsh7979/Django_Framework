from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Resume(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=100)
    skill=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    work_experience=models.CharField(max_length=100)
    projects=models.CharField(max_length=100)
    certificates=models.CharField(max_length=100)
    language=models.CharField(max_length=100)
    intrests=models.CharField(max_length=100)


# class likes(Resume):
#     like=models.IntegerField()



class likes(Resume):
    myuser=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,parent_link=True)
    like=models.IntegerField()


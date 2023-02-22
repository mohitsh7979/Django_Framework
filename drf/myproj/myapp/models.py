from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=50, null=True , blank=True)
    address=models.CharField(max_length=50 ,null=True , blank=True)
    roll=models.IntegerField()

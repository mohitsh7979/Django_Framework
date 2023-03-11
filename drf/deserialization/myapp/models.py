from django.db import models

# Create your models here.


class deserailization(models.Model):
    name=models.CharField(max_length=30,blank=True,null=True)
    age=models.IntegerField(blank=True , null=True)
    address=models.CharField(max_length=30,blank=True,null=True)

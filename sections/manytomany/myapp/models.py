from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class formmodel(models.Model):
    a=models.ManyToManyField(User)
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=10)

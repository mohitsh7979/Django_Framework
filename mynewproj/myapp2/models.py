from django.db import models

# Create your models here.


class mymodel(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=20)
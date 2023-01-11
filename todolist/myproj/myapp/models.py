from django.db import models

# Create your models here.

class listmodel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    course=models.CharField(max_length=50)


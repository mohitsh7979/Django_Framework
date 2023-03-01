from django.db import models
from django.contrib.auth.models import User


# Create your models her


class formmodel(models.Model):
    # a=models.OneToOneField(User, on_delete=models.CASCADE)
    # a=models.OneToOneField(User, on_delete=models.PROTECT)
    # a=models.OneToOneField(User, on_delete=models.PROTECT,primary_key=True,limit_choices_to={'is_staff':True})
    a=models.ManyToManyField(User)
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=10)
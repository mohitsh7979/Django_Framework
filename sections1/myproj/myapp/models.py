from django.db import models

# Create your models here.


class Farmer(models.Model):
    s_no=models.AutoField(primary_key=True,default=1)
    name=models.CharField(max_length=30)
    Father_name=models.CharField(max_length=30,null=True,blank=True)
    address=models.CharField(max_length=30)
    village=models.CharField(max_length=30)
    mobile_no=models.IntegerField()




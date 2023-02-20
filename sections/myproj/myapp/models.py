from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    roll_no=models.IntegerField()
    father_name=models.CharField(max_length=100)
    date=models.DateTimeField()
    image=models.ImageField(upload_to="media")

    


   

    
            
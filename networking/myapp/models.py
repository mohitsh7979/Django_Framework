from django.db import models

# Create your models here.



class regex_networking_model(models.Model):
    student_name = models.CharFieldl(max_length = 100)
    course_name = models.CharField(max_length = 100)
    referel_code = models.CharField(max_length=50)


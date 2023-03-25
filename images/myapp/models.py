from django.db import models

# Create your models here.


class image_upload(models.Model):
    pan_card = models.ImageField(upload_to='media')
    aadhar_card = models.ImageField(upload_to='media')

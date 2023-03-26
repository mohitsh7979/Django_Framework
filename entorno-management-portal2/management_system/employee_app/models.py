from django.db import models

# Create your models here.


class Employee_model(models.Model):

    GENDER = (

        ('m', 'male'),
        ('f', 'female'),
        ('o', 'other'),
    )

    DEEIGNATION = (

        ('s', 'Sales Officer'),
        ('t', 'Territory Exceutive'),
        ('f', 'Field Assistant'),
        ('g', 'General Manager'),
        ('h', 'HR Manager'),
        ('o', 'Office Management Staff'),
        ('c', 'CA'),
        ('d', 'Director'),
        ('D', 'Desk Office Assitant'),


    )
    profile_pic = models.ImageField(upload_to='media/profile_pic')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile_no = models.IntegerField(null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=100)
    designation = models.CharField(choices= DEEIGNATION, max_length=100)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    pan_card = models.ImageField(upload_to='media/pan_card')
    adhar_card = models.ImageField(upload_to='media/adhar_card')
    cheque = models.ImageField(upload_to='media/bank_details')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.username

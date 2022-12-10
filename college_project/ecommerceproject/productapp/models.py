from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES=(
    ('m','men'),
    ('w','women'),
    ('k','kids'),
    ('mk','men kit'),
    ('wt','watch'),
    ('f','featured_product'),
    ('l','latest_product'),
    ('b','brands'),
    ('t','testimonial'),
    ('o','offers'),
    ('ban','banner'),
)


class Product(models.Model):
    title=models.CharField(max_length=100)
    price=models.IntegerField()
    desc=models.CharField(max_length=1000)
    catagory=models.CharField(choices=CATEGORY_CHOICES,max_length=50)
    images=models.ImageField(upload_to='media/productimages')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

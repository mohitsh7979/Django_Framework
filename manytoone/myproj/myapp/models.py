from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)  # cascade method if we want to delete my post with my page not user 
    # user=models.ForeignKey(User,on_delete=models.PROTECT)  # protect method when we applid when if we want to delete my post with post user 
    # user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True) # Null method we used when we want that user is detelet but post is stay
    post_Title=models.CharField(max_length=100)
    post_content=models.CharField(max_length=100)
    post_date=models.DateTimeField()
    



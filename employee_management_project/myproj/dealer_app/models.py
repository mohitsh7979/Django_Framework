from django.db import models

# Create your models here.

class Dealer(models.Model):
    Business_Name=models.CharField(max_length=50)
    Mobile_No=models.IntegerField(null=True,blank=True)
    Whatsapp_No=models.IntegerField(null=True , blank=True)
    Address=models.CharField(max_length=30)
    District=models.CharField(max_length=30)
    Pin_code=models.IntegerField(null=True , blank=True)
    Gst_No=models.CharField(max_length=30,null=True , blank=True)
    Seed_License=models.CharField(max_length=30,null=True , blank=True)

    def __str__(self):
        return str(self.Business_Name)

class Distributer(models.Model):
    user=models.ForeignKey(Dealer,on_delete=models.CASCADE)
    Business_Name=models.CharField(max_length=50)
    Mobile_No=models.IntegerField(null=True,blank=True)
    Whatsapp_No=models.IntegerField(null=True , blank=True)
    Address=models.CharField(max_length=30)
    District=models.CharField(max_length=30)
    Pin_code=models.IntegerField(null=True , blank=True)
    Gst_No=models.CharField(max_length=30,null=True , blank=True)
    Seed_License=models.CharField(max_length=30,null=True , blank=True)

    
    


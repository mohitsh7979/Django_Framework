from django.contrib import admin
from .models import Dealer,Distributer

# Register your models here.

admin.site.register(Dealer)

# @admin.register(Dealer)

# class DealerAdmin(admin.ModelAdmin):
#     list_display=["id","Business_Name","Mobile_No","Whatsapp_No","Address","District","Pin_code","Gst_No","Seed_License"]




@admin.register(Distributer)

class farmerAdmin(admin.ModelAdmin):
    list_display=["id","user","Business_Name","Mobile_No","Whatsapp_No","Address","District","Pin_code","Gst_No","Seed_License"]




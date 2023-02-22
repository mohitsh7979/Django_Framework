from django.contrib import admin
from .models import Farmer


# Register your models here.

# admin.site.register(Farmer)

@admin.register(Farmer)

class Myadmin(admin.ModelAdmin):
    list_display=["s_no","name","Father_name","address","village","mobile_no"]

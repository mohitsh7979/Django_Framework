from django.contrib import admin
from .models import deserailization

# Register your models here.

@admin.register(deserailization)

class Myadmin(admin.ModelAdmin):
    list_display=["id","name","age","address"]



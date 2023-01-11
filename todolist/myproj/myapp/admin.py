from django.contrib import admin
from .models import listmodel

# Register your models here.

@admin.register(listmodel)

class listAdmin(admin.ModelAdmin):
    list_display=['id','name','email','course']


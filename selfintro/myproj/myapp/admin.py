from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display=['name','skill','address','user']

@admin.register(likes)
class likeAdmin(admin.ModelAdmin):
    list_display=['like']


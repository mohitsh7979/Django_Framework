from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Chat)
class chat(admin.ModelAdmin):
    list_display=['id','content','times','group']


@admin.register(Group)
class group(admin.ModelAdmin):
    list_display=['id','chatgroup']
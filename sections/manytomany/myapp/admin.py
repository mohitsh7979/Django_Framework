from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(formmodel)


class Mymodel(admin.ModelAdmin):
    list_display=["name","age"]

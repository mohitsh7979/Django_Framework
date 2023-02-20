from django.contrib import admin
from .models import Student

# Register your models here.

admin.site.register(Student)
# @admin.register(Student)

# class studentadmin(admin.ModelAdmin):
#     list_display=['name','roll_no','father_name','date','image']   
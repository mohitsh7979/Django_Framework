from django.contrib import admin
from .models import resume

# Register your models here.

@admin.register(resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display=['name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_file']



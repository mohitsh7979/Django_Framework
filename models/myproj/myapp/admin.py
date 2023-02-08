from django.contrib import admin
from .models import Runner

# Register your models here.

@admin.register(Runner)
class RunnerAdmin(admin.ModelAdmin):
    list_display=['id','MedalType','name','medal']
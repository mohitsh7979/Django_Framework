from django.contrib import admin
from myapp2.models import mymodel
# Register your models here.


@admin.register(mymodel)

class Mymodeladmin(admin.ModelAdmin):
    list_display=["id","name","age"]



from django.contrib import admin
from django.urls import path,include
from employee_app import views

urlpatterns = [
 
    path('employee_add/',views.employee),


]
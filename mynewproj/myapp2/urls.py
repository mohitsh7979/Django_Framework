from django.contrib import admin
from django.urls import path
from myapp2 import views

urlpatterns = [
  
    path('home/',views.home),
    path('data/<int:a>/',views.mydata)
]


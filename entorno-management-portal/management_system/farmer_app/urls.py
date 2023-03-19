from django.contrib import admin
from django.urls import path,include
from farmer_app import views

urlpatterns = [
 
    path('farmer_form/',views.farmer_detail),
    path('farmer_detail/',views.farmer),
   

]
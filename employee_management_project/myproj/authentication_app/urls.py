

from django.urls import path
from authentication_app import views

urlpatterns = [

    path('login/', views.loginhandle),
    path('signup/', views.signup),
    path('logout/', views.logouthandle),


]

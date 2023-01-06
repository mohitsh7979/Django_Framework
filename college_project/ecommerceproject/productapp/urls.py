
from django.contrib import admin
from django.urls import path
from productapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.product),
    path('productview/<int:id>',views.productview),
    path('addcart/',views.addcart),
    path('showcart/',views.showcart),
    path('checkout/',views.checkout),
    path('paymentdone/',views.Orderplaced),
    path('header/',views.header),
    path('men/',views.men),
    path('women/',views.women),
    path('kids/',views.kids),
    path('delete/<int:id>/',views.productdelete),
  
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

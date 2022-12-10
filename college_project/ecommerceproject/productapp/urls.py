
from django.contrib import admin
from django.urls import path
from productapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('product/',views.product),
    path('productview/<int:id>',views.productview),
    path('addcart/',views.addcart),
    path('showcart/',views.showcart),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

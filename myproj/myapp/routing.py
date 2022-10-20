from django.urls import path
from .import consumers

websocket_urlpatterns=[
    path('ws/sc/',consumers.MySynconsumer.as_asgi()),
    path('ws/ac/',consumers.myasynconsumer.as_asgi()),

]
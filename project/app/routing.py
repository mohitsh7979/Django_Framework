from django.urls import path
from .import consumers

websocket_urlpatterns=[
    path('ws/sc/',consumers.Myconsumer.as_asgi()),
    path('ws/ac/',consumers.Myasynconsumer.as_asgi()),
]

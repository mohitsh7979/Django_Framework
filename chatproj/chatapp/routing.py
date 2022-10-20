from more_itertools import consumer
from .import consumers
from django.urls import path

websocket_urlpatterns = [
    path('ws/sc/<str:groupname>/',consumers.Mysynconsumer.as_asgi()),
    path('ws/ac/',consumers.Myaynconsumer.as_asgi()),
]
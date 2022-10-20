"""
ASGI config for chatproj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
import chatapp.routing



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatproj.settings')

application = ProtocolTypeRouter({
   'http':get_asgi_application(),
   'websocket':URLRouter(
    chatapp.routing.websocket_urlpatterns
   )


})

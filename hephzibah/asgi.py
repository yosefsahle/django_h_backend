import os
from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from hephzibah import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hephzibah.settings')

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter(
#                 [
#                     # Define your WebSocket URL routes here
#                     # e.g., path("ws/some_path/", consumers.SomeConsumer.as_asgi()),
#                 ]
#             )
#         )
#     ),
# })

websocket_urlpatterns = [
    path('ws/group/<int:group_id>/notifications/', consumers.GroupNotificationConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})

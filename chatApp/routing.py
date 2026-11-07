from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/cc/<str:roomkanaam>/', consumers.ChatConsumer.as_asgi())

]
from django.urls import path
from .consumers import CouriersConsumer

websocket_urlpatterns = [
    path('ws/couriers/', CouriersConsumer.as_asgi()),
]

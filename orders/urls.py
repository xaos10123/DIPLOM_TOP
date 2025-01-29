from django.urls import path
from .views import *

app_name = "orders"

urlpatterns = [
    path("create_order/", create_order, name="create_order"),
    path("send_order/", send_order, name="send_order"),
    path("payment_order/<int:order_id>", payment_order, name="payment_order"),
    
]

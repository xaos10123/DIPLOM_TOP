from django.urls import path

from delivery_panel.views import list_delivery, get_order, my_delivery, close_order

app_name = "delivery"

urlpatterns = [
    path("", list_delivery, name="delivery_panel"),
    path('get_order/<int:pk>', get_order, name='get_order'),
    path('my_delivery/', my_delivery, name='my_delivery'),
    path('close_order/<int:pk>', close_order, name='close_order'),
]

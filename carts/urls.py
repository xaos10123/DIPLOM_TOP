from django.urls import path
from carts.views import *

app_name = 'cart'

urlpatterns = [
    path('cart_add/<slug:product_slug>', cart_add, name='cart_add'),
    path('cart_change/<int:cart_id>/<slug:to>', cart_change, name='cart_change'),
    path('cart_remove/<int:cart_id>', cart_remove, name='cart_remove'),
    path('get-count/', get_cart_count, name='get_count'),
]
import json
from os import name
from django.http import HttpResponse
from django.shortcuts import render

from carts.models import Cart
from goods.models import Product


def cart_add(request, product_slug):
    prod = Product.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=prod)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=prod, quantity=1)

    response = HttpResponse()
    response['HX-Trigger'] = json.dumps({
        'showNotification': {
            'message': f'{prod.name} {prod.char} добавлен в корзину.',
            'type': 'primary'
        }
    })
    return response


def cart_change(request, product_slug):
    pass


def cart_remove(request, product_slug):
    pass

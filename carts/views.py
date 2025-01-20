import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from carts.models import Cart
from goods.models import Product


def cart_add(request, product_slug):
    if not request.user.is_authenticated:
        response = HttpResponse()
        response['HX-Trigger'] = json.dumps({
            'showModal': {
                'url': reverse('user:login')
            }
        })
        return response
    
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
        },
        'updateCartCount': True
    })
    return response

@login_required
def cart_change(request, product_slug):
    pass

@login_required
def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    prod = cart.product
    cart.delete()

    response = HttpResponse()
    response['HX-Trigger'] = json.dumps({
        'showNotification': {
            'message': f'{prod.name} {prod.char} удален из корзины!',
            'type': 'danger'
        },
        'updateCartCount': True
    })
    return response

@login_required
def get_cart_count(request):
    count = Cart.objects.filter(user=request.user).total_quantity()
    return render(request, 'carts/cart_count.html', {'count': count})


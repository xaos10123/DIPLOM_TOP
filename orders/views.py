import json
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import render

from carts.models import Cart
from orders.models import Order, OrderItem
from users.models import Adress


@login_required
def create_order(request): 
    return render(request, 'orders/create_order.html')

@login_required
def send_order(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                user = request.user
                cart_items = Cart.objects.filter(user=user)

                if cart_items.exists():
                    order = Order.objects.create(
                        user = user,
                        adress = Adress.objects.filter(user=user, is_active=True).first(),
                    )

                    for cart_item in cart_items:
                        product = cart_item.product
                        name = f'{cart_item.product.name} {cart_item.product.char}'
                        price = cart_item.product.sell_price()
                        quantity = cart_item.quantity

                        if product.quantity < quantity:
                            raise ValidationError(f'На складе недостаточно товара {name}. Остаток: {product.quantity}шт.')
                        
                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            name=name,
                            price=price,
                            quantity=quantity
                        )
                        product.quantity -= quantity
                        product.order_amount += quantity
                        product.save()
                    
                    cart_items.delete()
                    
                    return render(request, 'orders/send_order.html')

        except ValidationError as e:
            response = HttpResponse()
            response['HX-Trigger'] = json.dumps({
            'showNotification': {
                'message': str(e),
                'type': 'danger'
            },
            # 'updateCartCount': True,
            # 'updateCartList': True
            })
            return response

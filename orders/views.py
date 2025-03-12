import json
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


from carts.models import Cart
from orders.models import Order, OrderItem
from users.models import Adress


@login_required
def create_order(request):
    return render(request, "orders/create_order.html")


@login_required
def payment_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.is_paid = True
    order.status = "В сборке"
    order.save()

    items = OrderItem.objects.filter(order=order)
    for item in items:
        item.product.order_amount += item.quantity
        item.product.quantity -= item.quantity
        item.product.save()

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "couriers",
        {
            "type": "new_order",
            "message": {
                "order_id": order.id,
                "adress": str(order.adress),
                "items": [
                    {"name": item.name, "quantity": item.quantity}
                    for item in order.items.all()
                ],
            },
        },
    )

    return render(request, "orders/payment.html", {"order": order})


@login_required
def send_order(request):
    if request.method == "POST":
        try:
            with transaction.atomic():
                user = request.user
                cart_items = Cart.objects.filter(user=user)

                if cart_items.exists():
                    order = Order.objects.create(
                        user=user,
                        adress=Adress.objects.filter(user=user, is_active=True).first(),
                    )

                    for cart_item in cart_items:
                        product = cart_item.product
                        name = f"{cart_item.product.name} {cart_item.product.char}"
                        price = cart_item.product.sell_price()
                        quantity = cart_item.quantity

                        if product.quantity < quantity:
                            raise ValidationError(
                                f"На складе недостаточно товара {name}. Остаток: {product.quantity}шт."
                            )

                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            name=name,
                            price=price,
                            quantity=quantity,
                        )

                    cart_items.delete()

                    return render(request, "orders/send_order.html", {"order": order})

        except ValidationError as e:
            response = HttpResponse()
            response["HX-Trigger"] = json.dumps(
                {
                    "showNotification": {"message": str(e), "type": "danger"},
                    "updateCartCount": True,
                    "updateCartList": True,
                }
            )
            return response

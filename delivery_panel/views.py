from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from orders.models import Order


@login_required
def list_delivery(request):
    order = Order.objects.filter(is_paid=True, delivery_man=None).order_by("-id")
    return render(request, "delivery_panel/delivery_panel.html", {"orders": order})


@login_required
def get_order(request, pk):
    order = Order.objects.get(pk=pk)
    if not order.delivery_man:
        order.delivery_man = request.user
        order.status = "В доставке"
        order.save()
    return redirect(to="delivery:my_delivery")


@login_required
def my_delivery(request):
    order = Order.objects.filter(delivery_man=request.user, is_paid=True)
    return render(request, "delivery_panel/delivery_panel.html", {"orders": order})

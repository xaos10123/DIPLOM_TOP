from django import template

from carts.models import Cart

register = template.Library()

@register.simple_tag()
def user_carts(request):
    return Cart.objects.filter(user=request.user)

@register.simple_tag
def get_cart_items_count(user):
    if user.is_authenticated:
        return Cart.objects.filter(user=user).total_quantity()
    return 0
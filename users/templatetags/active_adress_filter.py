from django import template

register = template.Library()

@register.simple_tag
def get_active_address(user):
    return user.addresses.filter(is_active=True).first()

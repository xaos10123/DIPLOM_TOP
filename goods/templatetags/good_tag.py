from django import template

register = template.Library()

@register.filter
def truncate_and_pad(value, length):
    if len(value) > length:
        return value[:length - 3] + '...'
    else:
        return value.ljust(length, ' ')
from django import template

register = template.Library()

@register.filter
def endswith(value, arg):
    """Checks if a value ends with a certain string"""
    return str(value).endswith(str(arg))

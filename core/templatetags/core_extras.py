from django import template

register = template.Library()


@register.filter
def mul(value, arg):
    try:
        value = int(value)
        arg = int(arg)
        if arg: return value * arg
    except:
        pass
    return ''


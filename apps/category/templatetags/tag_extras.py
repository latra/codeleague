from django.template import Library

register = Library()


@register.filter(name='hash')
def hash(h, key):
    return h[key]

from django import template
from django.utils.html import mark_safe
register = template.Library()


@register.simple_tag()
def model_type(model_object):
    return model_object.__class__.__name__.lower()

from django import template
from django.utils.html import mark_safe
register = template.Library()


@register.simple_tag()
def include_anything(file_name):
    return mark_safe(open(file_name).read())
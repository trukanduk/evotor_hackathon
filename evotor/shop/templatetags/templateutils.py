from django import template
import json
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name="emptylist", is_safe=False, autoescape=False, needs_autoescape=True)
def emptylist(datum, autoescape=False):
    return mark_safe(datum or '[]')

@register.filter(name="emptydict", is_safe=False, autoescape=False, needs_autoescape=True)
def emptydict(datum, autoescape=False):
    return mark_safe(datum or '{}')

@register.filter(name="json", is_safe=False, autoescape=False, needs_autoescape=True)
def jsonf(datum, autoescape=False):
    return mark_safe(json.dumps(datum))

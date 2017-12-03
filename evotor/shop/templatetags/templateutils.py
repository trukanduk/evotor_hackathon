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

@register.filter(name="minus")
def minusf(val, val2):
    return float(val) - float(val2)

@register.filter(name="marja")
def marja(val1, val2):
    return 100.0 * (float(val1) - float(val2)) / (float(val1))

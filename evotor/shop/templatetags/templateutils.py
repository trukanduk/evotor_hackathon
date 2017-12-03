from django import template
import json
from django.utils.safestring import mark_safe
from random import choice

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

@register.filter(name="status2bootstrap")
def status2bootstrap(v):
    if v < 10:
        return 'error'
    elif v < 90:
        return 'success'
    else:
        return 'primary'

@register.filter(name="getstatus")
def getstatus(v, m):
    v = float(v)
    m, mm = map(int, m.split('-'))
    return min(v, mm) - m

@register.filter(name="pickrandname")
def pickrand(iterable):
    return choice(iterable)


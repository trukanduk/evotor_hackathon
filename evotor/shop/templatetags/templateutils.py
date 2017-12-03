from django import template
import json
from django.utils.safestring import mark_safe
from random import choice, random

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
def status2bootstrap(v, always=False):
    if v < 10:
        return '-danger'
    elif v < 90:
        return '' if not always else '-success'
    else:
        return '-primary'

@register.filter(name="getstatus")
def getstatus(v, m):
    v = float(v)
    m, mm = map(int, m.split('-'))
    return min(v, mm) - m

@register.filter(name="pickrandname")
def pickrand(iterable):
    return choice(iterable)

@register.filter(name="getminpairsuggname")
def getminpairsuggname(pair_suggestion):
    # raise ValueError(pair_suggestion)
    try:
        if float(pair_suggestion[1][5]) < float(pair_suggestion[1][6]):
            return pair_suggestion[1][3]
        else:
            return pair_suggestion[1][4]
    except:
        return pair_suggestion[1][4]

@register.filter(name="getoptimizedpairsuggestcost")
def getoptimizedpairsuggestcost(pair_suggestion, ratio=0.15):
    try:
        if float(pair_suggestion[1][5]) < float(pair_suggestion[1][6]):
            return 0.01 * float(pair_suggestion[1][5]) * (100.0 - ratio)
        else:
            return 0.01 * float(pair_suggestion[1][6]) * (100.0 - ratio)
    except:
        return 0.01 * float(pair_suggestion[1][6]) * (100.0 - ratio)

@register.filter(name="randnum")
def randnum(m, mm):
    return int(random() * (float(mm) - float(m)) + float(m))


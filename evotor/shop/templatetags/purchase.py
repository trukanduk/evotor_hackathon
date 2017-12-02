from django import template

register = template.Library()

@register.filter(name="status2bootstrap")
def status2bootstrap(value):
    return {
        'ok': 'success',
        'in-progress': 'primary',
        'draft': 'dark',
    }.get(value, 'error')

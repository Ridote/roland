from django import template

register = template.Library()

@register.filter
def get(value, arg):
    return value[arg]
@register.filter
def all(value):
	return value.all()
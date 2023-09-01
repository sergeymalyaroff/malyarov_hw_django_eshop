from django import template
from django.conf import settings

register = template.Library()

@register.filter
def mediapath(value):
    return f"{settings.MEDIA_URL}{value}"

@register.simple_tag
def mediapath_tag(value):
    return mediapath(value)

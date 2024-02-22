import datetime

from django import template
from django.conf import settings
from wagtail.images.models import Image

register = template.Library()


@register.filter
def chunks(value_list, chunk_size):
    """Return a list of chunks in a predefined size"""
    return [value_list[i : i + chunk_size] for i in range(0, len(value_list), chunk_size)]


@register.filter
def to_float(value):
    """Return value as float"""
    return float(value)


@register.filter(name="unix_to_datetime")
def unix_to_datetime(value):
    return datetime.datetime.fromtimestamp(int(value))


@register.simple_tag
def live_reload():
    """Check the boolean value of the given setting."""
    return getattr(settings, "LIVE_RELOAD", False)


@register.simple_tag
def get_me_image():
    id = getattr(settings, "ME_IMAGE_ID")
    return Image.objects.filter(pk=id).first()

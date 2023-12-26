import datetime

from django import template

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

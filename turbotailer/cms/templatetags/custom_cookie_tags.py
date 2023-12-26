from cookie_consent.models import CookieGroup
from django import template

register = template.Library()


@register.simple_tag
def get_all_cookies():
    """Return all cookiegroups"""
    return CookieGroup.objects.all().prefetch_related("cookie_set")

from django.conf import settings


def allauth_settings(request):
    """Expose some settings from django-allauth in templates."""
    return {
        "ACCOUNT_ALLOW_REGISTRATION": settings.ACCOUNT_ALLOW_REGISTRATION,
        "ROBOTS_META_CONTENT": getattr(settings, "ROBOTS_META_CONTENT", "index"),
    }

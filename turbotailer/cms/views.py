from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.core.cache import cache
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_GET


@require_GET
def robots_txt(request):
    lines = settings.ROBOTS
    return HttpResponse("\n".join(lines), content_type="text/plain")


@staff_member_required
def clear_cache_view(request):
    cache.clear()
    # Redirect to Wagtail admin home or a success message page
    return HttpResponseRedirect(reverse("wagtailadmin_home"))

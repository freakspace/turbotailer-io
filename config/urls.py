from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    path("", include("turbotailer.cms.urls")),
    path("", include("turbotailer.core.urls")),
    path("users/", include("turbotailer.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    path("dashboard/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("cookies/", include("cookie_consent.urls")),
    # For anything not caught by a more specific rule above, hand over to
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(path("", include(wagtail_urls)), prefix_default_language=False)
if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls)),
        ] + urlpatterns

    if settings.LIVE_RELOAD:
        urlpatterns = [
            path("__reload__/", include("django_browser_reload.urls")),
        ] + urlpatterns

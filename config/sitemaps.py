from django.contrib.sitemaps import views as sitemap_views
from wagtail.contrib.sitemaps.sitemap_generator import Sitemap


class CustomSitemap(Sitemap):
    def items(self):
        return (
            self.get_wagtail_site()
            .root_page.localized.get_descendants(inclusive=True)
            .live()
            .public()
            .order_by("path")
            .specific()
        )


def sitemap(request, **kwargs):
    sitemaps = {"wagtail": CustomSitemap(request)}
    return sitemap_views.sitemap(request, sitemaps, **kwargs)

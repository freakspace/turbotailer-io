from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from wagtail import hooks
from wagtail.admin.menu import MenuItem
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup

from .models import FooterText, SiteInfo


class FooterTextViewSet(SnippetViewSet):
    model = FooterText
    search_fields = ("body",)


class BakerySnippetViewSetGroup(SnippetViewSetGroup):
    menu_label = "Bakery Misc"
    menu_icon = "utensils"  # change as required
    menu_order = 300  # will put in 4th place (000 being 1st, 100 2nd)
    items = FooterTextViewSet


class SiteSettingsAdmin(ModelAdmin):
    model = SiteInfo
    menu_label = "Site Information"
    menu_icon = "site"
    add_to_settings_menu = True
    exclude_from_explorer = False


@hooks.register("register_settings_menu_item")
def register_clear_cache_menu_item():
    return MenuItem(
        _("Clear Cache"),
        reverse("cms:clear_cache"),
        classnames="icon icon-cog",
        order=1000,
    )


modeladmin_register(SiteSettingsAdmin)
register_snippet(FooterTextViewSet)

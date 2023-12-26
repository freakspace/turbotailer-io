from django import template
from django.core.cache import cache
from wagtail.models import Page, Site

from turbotailer.cms.models import FooterText, SiteInfo

register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context):
    # This returns a core.Page. The main menu needs to have the site.root_page
    # defined else will return an object attribute error ('str' object has no
    # attribute 'get_children')
    return Site.find_for_request(context["request"]).root_page


def has_menu_children(page):
    # This is used by the top_menu property
    # get_children is a Treebeard API thing
    # https://tabo.pe/projects/django-treebeard/docs/4.0.1/api.html
    return page.get_children().live().in_menu().exists()


def has_children(page):
    # Generically allow index pages to list their children
    return page.get_children().live().exists()


def is_active(page, current_page):
    # To give us active state on main navigation
    return current_page.url_path.startswith(page.url_path) if current_page else False


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the Foundation menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag("tags/top_menu.html", takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = calling_page.url_path.startswith(menuitem.url_path) if calling_page else False

    return {
        "calling_page": calling_page,
        "menuitems": menuitems,
        # required by the pageurl tag that we want to use within this template
        "request": context["request"],
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag("tags/top_menu_children.html", takes_context=True)
def top_menu_children(context, parent, calling_page=None):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    for menuitem in menuitems_children:
        menuitem.has_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = calling_page.url_path.startswith(menuitem.url_path) if calling_page else False
        menuitem.children = menuitem.get_children().live().in_menu()

    return {
        "parent": parent,
        "menuitems_children": menuitems_children,
        # required by the pageurl tag that we want to use within this template
        "request": context["request"],
    }


@register.inclusion_tag("tags/breadcrumbs.html", takes_context=True)
def breadcrumbs(context):
    self = context.get("self")
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(self, inclusive=True).filter(depth__gt=1)
    return {
        "ancestors": ancestors,
        "request": context["request"],
    }


@register.inclusion_tag("cms/include/company_logo.html", takes_context=True)
def company_logo(context):
    site_info = context.get("site_info", "")
    return {"company_logo": site_info.company_logo if site_info else ""}


@register.simple_tag(takes_context=True)
def site_info(context):
    request = context.get("request")
    current_site = Site.find_for_request(request) if request else None

    cache_key = f"site_info_{current_site.id if current_site else 'default'}"
    site_info = cache.get(cache_key)

    if not site_info and current_site:
        site_info = SiteInfo.objects.filter(site=current_site).first()
        cache.set(cache_key, site_info, timeout=300)

    return site_info


@register.inclusion_tag("cms/include/footer_content.html", takes_context=True)
def get_footer_content(context):
    request = context.get("request")
    site_info = context.get("site_info", "")
    current_site = Site.find_for_request(request) if request else None

    cache_key = f"footer_text_{current_site.id if current_site else 'default'}"
    cached_footer_data = cache.get(cache_key)

    if cached_footer_data:
        footer_text, footer_columns = cached_footer_data
    else:
        instance = FooterText.objects.filter(live=True).first()
        footer_text = instance.body if instance else ""
        footer_columns = instance.footer_columns if instance else None
        cache.set(cache_key, (footer_text, footer_columns), timeout=300)

    return {"footer_text": footer_text, "footer_columns": footer_columns, "site_info": site_info}
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.http import HttpResponseForbidden
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, PageChooserPanel, PublishingPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import DraftStateMixin, Page, PreviewableMixin, RevisionMixin, Site
from wagtail.snippets.models import register_snippet
from wagtailmenus.models import AbstractMainMenuItem

from .blocks import BaseStreamBlock, FooterColumnBlock
from .forms import StandardPageForm


class StandardPage(Page):
    """
    A generic content page. On this demo site we use it for an about page but
    it could be used for any type of page content that only needs a title,
    image, introduction and body field
    """

    body = StreamField(BaseStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True)
    role = models.CharField(
        max_length=50,
        help_text="Restrict access to this page by role",
        blank=True,
        null=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("role"),
    ]

    # Used to add choices in page
    base_form_class = StandardPageForm

    def serve(self, request, *args, **kwargs):
        required_role = self.role

        if required_role and not request.user.groups.filter(name=required_role).exists():
            return HttpResponseForbidden("You don't have access to this page.")

        return super().serve(request, *args, **kwargs)


class FooterText(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    models.Model,
):
    """
    This provides editable text for the site footer. Again it is registered
    using `register_snippet` as a function in wagtail_hooks.py to be grouped
    together with the Person model inside the same main menu item. It is made
    accessible on the template via a template tag defined in base/templatetags/
    navigation_tags.py
    """

    body = RichTextField()
    footer_columns = StreamField(
        [("column", FooterColumnBlock())], null=True, blank=True, verbose_name="Footer columns", use_json_field=True
    )

    panels = [
        FieldPanel("body"),
        FieldPanel("footer_columns"),
        PublishingPanel(),
    ]

    def __str__(self):
        return "Footer text"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {"footer_text": self.body}


class SiteInfo(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE, related_name="custom_site_info")
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    company_logo = models.OneToOneField(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    company_favicon = models.OneToOneField(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    google_analytics = models.CharField(max_length=20, null=True, blank=True)
    google_ads = models.CharField(max_length=20, null=True, blank=True)
    tag_manager = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return "Site information"


@register_snippet
class Review(models.Model):
    name = models.CharField("Name", max_length=255)
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else self.content[:29]


class CustomMainMenuItem(AbstractMainMenuItem):
    """A custom menu item model to be used by ``wagtailmenus.MainMenu``"""

    menu = ParentalKey(
        "wagtailmenus.MainMenu",
        on_delete=models.CASCADE,
        related_name="custom_menu_items",  # important for step 3!
    )
    title_en = models.CharField(max_length=32, verbose_name="English Title")
    title_da = models.CharField(max_length=32, verbose_name="Danish Title")

    # Also override the panels attribute, so that the new fields appear
    # in the admin interface
    panels = (
        PageChooserPanel("link_page"),
        FieldPanel("link_url"),
        FieldPanel("url_append"),
        FieldPanel("link_text"),
        FieldPanel("title_en"),
        FieldPanel("title_da"),
        FieldPanel("allow_subnav"),
    )

from django.db import models
from django.utils.translation import gettext as _
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet

from turbotailer.cms.blocks import BaseStreamBlock


@register_snippet
class ArticleTopic(models.Model):
    """Topic to generate articles from"""

    link = models.CharField(_("Link to related article"), max_length=255, blank=True, null=True)
    prompt = models.TextField(help_text="A prompt to generate the article with", blank=True, null=True)
    is_ready = models.BooleanField(help_text="Determines if a article can be written", default=False)
    is_parsed = models.BooleanField(help_text="Determines if the link can be scraped and parsed", default=False)
    has_article = models.BooleanField(help_text="Determines if an article has been written", default=False)


# TODO Create task to create articles


class ArticlePage(Page):
    """A Article Page"""

    introduction = models.TextField(help_text="Text to describe the page", blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape mode only; horizontal width between 1000px and 3000px.",
    )
    body = StreamField(BaseStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True)
    subtitle = models.CharField(blank=True, max_length=255)
    date_published = models.DateField("Date article published", blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("introduction"),
        FieldPanel("image"),
        FieldPanel("body"),
        FieldPanel("date_published"),
    ]

    # Specifies parent to BlogPage as being BlogIndexPages
    parent_page_types = ["ArticleIndexPage"]

    # Specifies what content types can exist as children of BlogPage.
    # Empty list means that no child content types are allowed.
    subpage_types = []


class ArticleIndexPage(Page):
    """
    Index page for blogs.
    We need to alter the page model's context to return the child page objects,
    the BlogPage objects, so that it works as an index page

    RoutablePageMixin is used to allow for a custom sub-URL for the tag views
    defined above.
    """

    introduction = models.TextField(help_text="Text to describe the page", blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape mode only; horizontal width between 1000px and 3000px.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("image"),
    ]

    # Specifies that only BlogPage objects can live under this index page
    subpage_types = ["ArticlePage"]

    # Defines a method to access the children of the page (e.g. BlogPage
    # objects). On the demo site we use this on the HomePage
    def children(self):
        return self.get_children().specific().live()

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    # https://docs.wagtail.org/en/stable/getting_started/tutorial.html#overriding-context
    def get_context(self, request):
        context = super().get_context(request)
        context["articles"] = ArticlePage.objects.descendant_of(self).live().order_by("-date_published")
        return context

    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)

    # Returns the child BlogPage objects for this BlogPageIndex.
    # If a tag is used then it will filter the posts by tag.
    def get_posts(self):
        return ArticlePage.objects.live().descendant_of(self)

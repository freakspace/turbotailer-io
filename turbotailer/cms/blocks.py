from django.db.models import Avg
from wagtail.blocks import (
    BooleanBlock,
    CharBlock,
    ChoiceBlock,
    IntegerBlock,
    ListBlock,
    PageChooserBlock,
    RawHTMLBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

# TODO Add anchor block
# TODO Add empty space block
# TODO Make it possible to define CTA text globally
# TODO Fix cta button style being required
# TODO Fjern aws cli hvis muligt


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """

    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "blocks/image_block.html"


class HeadingBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to select h2 - h4 sizes for headers
    """

    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(
        choices=[
            ("", "Select a header size"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"


class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows the user to attribute a quote to the author
    """

    text = TextBlock()
    attribute_name = CharBlock(blank=True, required=False, label="e.g. Mary Berry")

    class Meta:
        icon = "openquote"
        template = "blocks/blockquote.html"


class Button(StructBlock):
    title = CharBlock(required=False, help_text="Button display text")
    page_link = PageChooserBlock(required=False, help_text="Select an internal page to link to")
    anchor = CharBlock(required=False, help_text="Link to a anchor on the same page")
    open_modal = BooleanBlock(required=False, help_text="Open form modal")
    style = ChoiceBlock(
        choices=[
            ("", "Select a style"),
            ("primary", "Primary"),
            ("secondary", "Secondary"),
            ("light", "Light"),
            ("dark", "Dark"),
        ],
        blank=False,
        required=False,
    )
    outline = BooleanBlock(required=False, help_text="Make the button outline?")

    class Meta:
        template = "blocks/cta_button.html"
        icon = "link"
        label = "Call to action button"


class USPBlock(StructBlock):
    text = CharBlock(required=False, help_text="USP text")

    class Meta:
        template = "blocks/usp_block.html"
        icon = "pick"
        label = "Unique Selling Point"


class HeroBlock(StructBlock):
    title = RawHTMLBlock(required=True, help_text="Add your title")
    sub_title = CharBlock(required=False, help_text="Add your sub title")
    image = ImageChooserBlock(required=True)
    buttons = ListBlock(Button(required=False))
    usps = ListBlock(USPBlock(required=False))
    full_width = BooleanBlock(required=False, help_text="Make hero full width")

    def get_form_context(self, value, prefix="", errors=None):
        context = super().get_form_context(value, prefix=prefix, errors=errors)
        context["heading_text"] = self.label  # Use the block's label as the collapsed title
        return context

    class Meta:
        template = "blocks/hero.html"
        icon = "image"
        label = "Hero Banner"


class EmptySpaceBlock(StructBlock):
    background_color = BooleanBlock(required=False, help_text="Add background color")

    class Meta:
        template = "blocks/empty_space_block.html"
        icon = "placeholder"
        label = "Empty Space"


class AccordionItemBlock(StructBlock):
    title = CharBlock(required=True, help_text="Add your title")
    content = RichTextBlock(required=True, help_text="Add your content")

    class Meta:
        template = "blocks/accordion_item_block.html"
        icon = "placeholder"
        label = "Accordion Item"


class AccordionBlock(StreamBlock):
    accordion_item = AccordionItemBlock()

    class Meta:
        template = "blocks/accordion_block.html"
        icon = "list-ul"
        label = "Accordion"


class ReviewBlock(StructBlock):
    max_count = IntegerBlock(required=False, help_text="Maximum number of reviews to display", default=10)

    def get_context(self, value, parent_context=None):
        from .models import Review

        context = super().get_context(value, parent_context=parent_context)
        max_count = value.get("max_count") or 10
        reviews = Review.objects.all()[:max_count]
        context["reviews"] = reviews
        context["reviews_count"] = Review.objects.count()
        context["average_rating"] = Review.objects.aggregate(Avg("rating"))["rating__avg"]
        return context

    class Meta:
        template = "blocks/reviews/review_block.html"


class ServicesItemBlock(StructBlock):
    title = CharBlock(required=False, help_text="Add your title, default to 'Your services'")
    image = ImageChooserBlock(required=True)
    page_link = PageChooserBlock(required=False, help_text="Select an internal page to link to")

    class Meta:
        template = "blocks/services_item_block.html"
        icon = "doc-empty-inverse"
        label = "Services item"


class ServicesBlock(StructBlock):
    title = CharBlock(required=True, help_text="Add your title")
    services = ListBlock(ServicesItemBlock())

    class Meta:
        template = "blocks/services_block.html"
        icon = "info-circle"
        label = "Services"
        collapsed = True


class CasesItemBlock(StructBlock):
    title = CharBlock(required=False, help_text="Add your title")
    image = ImageChooserBlock(required=True)
    page_link = PageChooserBlock(required=False, help_text="Select an internal page to link to")

    class Meta:
        template = "blocks/cases_item_block.html"
        icon = "doc-empty-inverse"
        label = "Cases item"


class CasesBlock(StructBlock):
    title = CharBlock(required=False, help_text="Add your title")
    subtitle = CharBlock(required=False, help_text="Add your subtitle")
    description = RichTextBlock(required=True, help_text="Add your description")
    cases = ListBlock(CasesItemBlock())

    class Meta:
        template = "blocks/cases_block.html"
        icon = "info-circle"
        label = "Cases"
        collapsed = True


class FeaturesItemBlock(StructBlock):
    title = CharBlock(required=False, help_text="Add your title")
    description = CharBlock(required=False, help_text="Add your description")
    icon = ImageChooserBlock(required=True)

    class Meta:
        template = "blocks/features_item_block.html"
        icon = "doc-empty-inverse"
        label = "Feature"


class FeaturesBlock(StructBlock):
    title = CharBlock(required=False, help_text="Add your title")
    features = ListBlock(FeaturesItemBlock())

    class Meta:
        template = "blocks/features_block.html"
        icon = "info-circle"
        label = "Features"
        collapsed = True


class AnchorBlock(StructBlock):
    anchor_tag = CharBlock(required=False, help_text="Write a tag you remember")

    class Meta:
        template = "blocks/anchor_block.html"
        icon = "info-circle"
        label = "Anchor"
        collapsed = True


class TextImageBlock(StructBlock):
    subtitle = CharBlock(required=False, help_text="Add your subtitle")
    title = CharBlock(required=True, help_text="Add your title")
    text = RichTextBlock(required=True, help_text="Add your text")
    image = ImageChooserBlock(required=False)
    embed = EmbedBlock(
        required=False,
        help_text="Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
        max_width=800,
        max_height=400,
    )
    buttons = ListBlock(Button(required=True))
    reverse = BooleanBlock(required=False, help_text="Reverse the order of text and image")
    shadow = BooleanBlock(required=False, help_text="Add a shadow to image")

    class Meta:
        template = "blocks/text_image_block.html"
        icon = "info-circle"
        label = "Text & Image"


class PageItemBlock(StructBlock):
    title = CharBlock(required=True, help_text="Add your title")
    page = PageChooserBlock(required=False)

    class Meta:
        template = "blocks/page_list_item.html"


class PageListBlock(StructBlock):
    title = CharBlock(required=True, help_text="Add your title")
    text = TextBlock(required=False, help_text="Add your text")
    pages = ListBlock(PageItemBlock())

    class Meta:
        template = "blocks/page_list_block.html"
        icon = "info-circle"
        label = "List with pages"


class HighlightBlock(StructBlock):
    title = CharBlock(required=True, help_text="Add your title")
    button = Button(required=True)

    class Meta:
        template = "blocks/highlight_block.html"
        icon = "info-circle"
        label = "Highlight something"


class FooterLinkBlock(StructBlock):
    title = CharBlock(required=True, max_length=50)
    page = PageChooserBlock(required=False)

    class Meta:
        template = "blocks/footer_link_block.html"
        icon = "link"


class FooterColumnBlock(StructBlock):
    heading = CharBlock(required=False, max_length=50)
    links = ListBlock(FooterLinkBlock())

    class Meta:
        template = "blocks/footer_column_block.html"
        icon = "list-ul"


class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """

    heading = HeadingBlock()
    paragraph = RichTextBlock(icon="pilcrow", template="blocks/paragraph_block.html")
    image = ImageBlock()
    block = BlockQuote()
    accordion = AccordionBlock(label_format="FAQ (Accordion)")
    hero = HeroBlock(label_format="Hero")
    review = ReviewBlock(label_format="Reviews")
    services = ServicesBlock(label_format="Services")
    cases = CasesBlock(label_format="Cases")
    features = FeaturesBlock(label_format="Features")
    text_image = TextImageBlock(label_format="Text & Image")
    page_list = PageListBlock(label_format="List with pages")
    highlight = HighlightBlock(label_format="Highlight")
    anchor = AnchorBlock(label_format="Anchor")
    empty_space = EmptySpaceBlock(label_format="Empty Space")

    class Meta:
        block_counts = {"accordion": {"min_num": 0, "max_num": 1}}
        collapsed = True

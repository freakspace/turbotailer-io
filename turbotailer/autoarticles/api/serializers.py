from django.utils.text import slugify
from rest_framework import serializers

from turbotailer.autoarticles.models import ArticleIndexPage, ArticlePage, ArticleTopic


def generate_unique_slug(parent_page, title):
    base_slug = slugify(title)
    slug = base_slug
    i = 1
    while parent_page.get_children().filter(slug=slug).exists():
        slug = f"{base_slug}-{i}"
        i += 1
    return slug


class ArticleTopicSerializer(serializers.ModelSerializer):
    """
    Serializer for the ArticleTopic model.
    """

    class Meta:
        model = ArticleTopic
        fields = (
            "link",
            "prompt",
        )


class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializer for the ArticlePage model.
    """

    locale_id = serializers.IntegerField(required=False)

    class Meta:
        model = ArticlePage
        fields = (
            "locale_id",
            "title",
            "body",
            "seo_title",
            "search_description",
        )

    def create(self, validated_data):
        # Get parent page with correct language
        parent_page = ArticleIndexPage.objects.get(locale_id=validated_data.get("locale_id"))

        # Generate a slug from the title
        validated_data["slug"] = generate_unique_slug(parent_page, validated_data.get("title"))

        # Create a new instance of ArticlePage without saving it
        article_page = ArticlePage(**validated_data)

        # Use Wagtail's method to add the page to the tree
        parent_page.add_child(instance=article_page)

        return article_page

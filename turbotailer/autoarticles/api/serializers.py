from rest_framework import serializers

from turbotailer.autoarticles.models import ArticleIndexPage, ArticlePage


class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializer for the ArticlePage model.
    """

    class Meta:
        model = ArticlePage
        fields = (
            "id",
            "title",
            "introduction",
            "image",
            "body",
            "subtitle",
            "date_published",
            "seo_title",
            "search_description",
        )

    def create(self, validated_data):
        parent_page = ArticleIndexPage.objects.first()

        # Create a new instance of ArticlePage without saving it
        article_page = ArticlePage(**validated_data)

        # Use Wagtail's method to add the page to the tree
        parent_page.add_child(instance=article_page)

        return article_page

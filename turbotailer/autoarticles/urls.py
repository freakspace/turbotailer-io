from django.urls import path

from turbotailer.autoarticles.api.views import article_create_view, topic_create_view

urlpatterns = [
    path("autoarticles/create/article", article_create_view, name="article-create"),
    path("autoarticles/create/topic", topic_create_view, name="topic-create"),
]

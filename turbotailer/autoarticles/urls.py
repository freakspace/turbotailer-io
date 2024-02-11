from django.urls import path

from turbotailer.autoarticles.api.views import (
    article_create_view,
    topic_create_view,
    topic_list_view,
    topic_update_view,
)

urlpatterns = [
    path("autoarticles/create/article", article_create_view, name="article-create"),
    path("autoarticles/create/topic", topic_create_view, name="topic-create"),
    path("autoarticles/topics", topic_list_view, name="topic-create"),
    path("autoarticles/topics/<int:topic_id>/", topic_update_view, name="update-topic"),
]

from django.urls import path

from turbotailer.autoarticles.api.views import article_create_view

urlpatterns = [
    path("autoarticles/create/", article_create_view, name="article-create"),
]

from django.urls import path

from .views import clear_cache_view, robots_txt

app_name = "cms"

urlpatterns = [
    path(route="robots.txt", view=robots_txt, name="robots"),
    path(route="clear_cache/", view=clear_cache_view, name="clear_cache"),
]

from django.urls import path

from .views import AuditCreateView

app_name = "core"

urlpatterns = [
    path("audit/create/", AuditCreateView.as_view(), name="audit_create_view"),
]

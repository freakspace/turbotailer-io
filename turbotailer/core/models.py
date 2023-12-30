from django.db import models
from django.utils.translation import gettext as _


class Audit(models.Model):
    """Requests for audits"""

    name = models.CharField(_("Navn"), max_length=255, blank=False, null=False)
    website = models.CharField(_("Hjemmeside"), max_length=100, blank=False, null=False)
    email = models.EmailField(_("E-mail"), max_length=100, blank=False, null=False)

    created = models.DateTimeField(auto_now_add=True)

    video_url = models.CharField(_("Video link"), max_length=255, blank=True, null=True)

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Audit


@receiver(post_save, sender=Audit)
def send_email(sender, instance, created, **kwargs):
    """
    Send e-mail after form submission
    """
    # TODO Not implemented yet
    pass

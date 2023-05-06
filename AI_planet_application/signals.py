from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage
from .models import Hackathon

@receiver(post_delete, sender=Hackathon)
def delete_upload(sender, instance, **kwargs):
    instance.background_image.delete(save=False)
    instance.hackathon_image.delete(save=False)
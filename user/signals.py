from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from .models import UserProfile, Address, TopMeasurement, BottomMeasurement

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        Address.objects.create(user=instance)
        TopMeasurement.objects.create(user = instance)
        BottomMeasurement.objects.create(user = instance)

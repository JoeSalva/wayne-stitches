from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from .models import UserProfile, Address

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.get_or_create(user=instance)
        Address.objects.get_or_create(profile = user_profile)
        
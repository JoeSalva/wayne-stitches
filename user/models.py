from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField  # type: ignore
from django.conf import settings
from order.choices import NigerianStates

# Create your models here.

class CustomUser(AbstractUser):
    phone = PhoneNumberField(region='NG', blank=True, null=True) # type: ignore

    def __str__(self) -> str:
        return self.username
    
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(upload_to='avatars/', default='avatars/userimage.png')

    class Meta:
        verbose_name_plural = 'User Profiles'

    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"
    
class Address(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, choices=NigerianStates.choices, blank=True)
    LGA = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=225, blank=True)

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self) -> str:
        return f"{self.user.username}'s Address"

class TopMeasurement(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Back_or_Shoulder = models.IntegerField(blank=True, null=True)
    Chest_or_Burst = models.IntegerField(blank=True, null=True)
    Stomach = models.IntegerField(blank=True, null=True)
    Length = models.IntegerField(blank=True, null=True)
    Neck = models.IntegerField(blank=True, null=True)
    Hand = models.IntegerField(blank=True, null=True)
    Arm = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s Top Measurement"

class BottomMeasurement(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Waist = models.IntegerField(blank=True, null=True)
    Lap = models.IntegerField(blank=True, null=True)
    Hip = models.IntegerField(blank=True, null=True)
    Knee = models.IntegerField(blank=True, null=True)
    Length = models.IntegerField(blank=True, null=True)
    Round_Ankle = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s Bottom Measurement"

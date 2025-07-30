from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField  # type: ignore
from django.conf import settings

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
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    country = models.CharField(max_length=15, blank=True)
    state = models.CharField(max_length=10, blank=True)
    local_gov_area = models.CharField(max_length=15, blank=True)
    street = models.CharField(max_length=50, blank=True)

class TopMeasurement(models.Model):
    Back_or_Shoulder = models.IntegerField()
    Chest_or_Burst = models.IntegerField()
    Stomach = models.IntegerField()
    Length = models.IntegerField()
    Neck = models.IntegerField()
    Hand = models.IntegerField()
    Arm = models.IntegerField()

    def __str__(self) -> str:
        return "Top Measurement"

class BottomMeasurement(models.Model):
    Waist = models.IntegerField()
    Lap = models.IntegerField()
    Hip = models.IntegerField()
    Knee = models.IntegerField()
    Length = models.IntegerField()
    Round_Ankle = models.IntegerField()

    def __str__(self) -> str:
        return "Bottom Measurement"

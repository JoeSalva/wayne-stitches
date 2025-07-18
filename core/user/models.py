from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    phone = PhoneNumberField(region='NG', blank=True, null=True) # type: ignore

    def __str__(self) -> str:
        return self.username
    
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='avatars/', default='avatars/userimage.png')

    class Meta:
        verbose_name_plural = 'User Profiles'

    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"
    
class Address(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    country = models.CharField(max_length=15)
    state = models.CharField(max_length=10)
    local_gov_area = models.CharField(max_length=15)
    street = models.CharField(max_length=50)
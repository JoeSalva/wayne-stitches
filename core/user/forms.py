from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField

User = get_user_model()

class CustomCreationForm(UserCreationForm):
    class Meta:
        phone = PhoneNumberField(region='NG', required=True)

        model = User
        fields = ('username', 'email', 'phone', 'password1', 'password2')
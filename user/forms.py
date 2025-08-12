from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField
from .models import UserProfile, Address, TopMeasurement, BottomMeasurement

User = get_user_model()

class CustomCreationForm(UserCreationForm):
    class Meta:
        phone = PhoneNumberField(region='NG', required=True)

        model = User
        fields = ('username', 'email', 'phone', 'password1', 'password2')

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture', 'nickname')

class UpdateAddress(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('country', 'state', 'LGA', 'street')

class UpdateTopMeasurements(forms.ModelForm):
    class Meta:
        model = TopMeasurement
        fields = ('Back_or_Shoulder', 'Chest_or_Burst', 'Stomach', 'Length', 'Neck', 'Hand', 'Arm')

class UpdateBottomMeasurements(forms.ModelForm):
    class Meta:
        model = BottomMeasurement
        fields = ('Waist', 'Lap', 'Hip', 'Knee', 'Length', 'Round_Ankle')



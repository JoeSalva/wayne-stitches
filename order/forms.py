from django import forms
from .models import Order
from .choices import NigerianStates

class DeliveryForm(forms.Form):
    delivery_state = forms.ChoiceField(
        choices=NigerianStates.choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

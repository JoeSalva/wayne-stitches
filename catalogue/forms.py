from django import forms
from .models import Product

class EditProductForm(forms.ModelForm): #type: ignore
    
    class Meta:
        model = Product
        fields = ("name", "slug", "image", "description", "category", "size", "price", "is_active")


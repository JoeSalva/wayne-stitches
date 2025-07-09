from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'order'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cart/remove/<int:id>', views.remove_from_cart, name='remove_from_cart')
]

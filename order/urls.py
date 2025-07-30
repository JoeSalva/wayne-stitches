from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'order'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cart/remove/<int:id>', views.remove_from_cart, name='remove_from_cart'),
    path('cart/create_order/<int:id>', views.create_order, name='create_order'),
    path('order_history/', views.order_history, name='order_history'),
]

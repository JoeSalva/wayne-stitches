from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'store'

urlpatterns = [
    path('catalogue/', views.store_front, name='store'),
    path('<slug:slug>', views.product, name='product_page'),
    path('cart/add/<int:id>', views.product_to_cart, name='product_to_cart'),
]

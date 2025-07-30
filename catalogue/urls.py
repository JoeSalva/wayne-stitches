from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'store'

urlpatterns = [
    path('catalogue/', views.store_front, name='store'),
    path('<slug:slug>', views.product, name='product_page'),
    path('category/<slug:slug>', views.category_view, name='category_view'),
    path('cart/add/<int:id>', views.product_to_cart, name='product_to_cart'),
    path('cart/edit_product/<int:id>', views.edit_product, name='edit_product'),
]

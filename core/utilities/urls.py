from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.searchbox, name='search'),
    path('filter/', views.price_filter, name='filter'),
]
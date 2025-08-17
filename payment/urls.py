from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'payment'

urlpatterns = [
    path("initiate/<int:id>/", views.initiate_payment_page, name="initiate_payment"),
    path('<int:id>/initiate', views.initialize_payment, name='initialize_payment'),
    path('verify/<int:id>/', views.verify_payment, name='verify_payment'),
]
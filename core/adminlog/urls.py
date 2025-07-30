from django.urls import path
from . import views

urlpatterns = [
    path('user_insight/', views.user_insight, name='insight'),
]
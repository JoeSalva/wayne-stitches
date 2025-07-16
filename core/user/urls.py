from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html', next_page='store:store'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('sign_up/', views.register, name='sign_up'),
]
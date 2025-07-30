from django.shortcuts import render
from django.contrib.auth import get_user_model, get_user
from order.models import Order


# Create your views here.


def user_insight(request):
    user = get_user_model()
    all_users = user.objects.all()
    return render(request, 'user_check.html', {'user':all_users,})
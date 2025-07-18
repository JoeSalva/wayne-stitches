from django.shortcuts import render, redirect
from .forms import CustomCreationForm, UpdateProfile, UpdateAddress
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import Group


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get_or_create(name='Customer')
            user.groups.add(group)
            return redirect('login')
    else:
        form = CustomCreationForm()
    return render(request, 'sign_up.html', {'form': form})

@login_required
@transaction.atomic
def update_profile(request):
    address = request.user.userprofile.address
    profile = request.user.userprofile

    if request.method == 'POST':
        p_form = UpdateProfile(request.POST, request.FILES, instance=profile)
        a_form = UpdateAddress(request.POST, instance=address)

        if p_form.is_valid() and a_form.is_valid():
            p_form.save()
            a_form.save()
            return redirect('user:profile')
    else:
        p_form = UpdateProfile(instance=profile)
        a_form = UpdateAddress(instance=address)
    return render(request, 'profile.html', {'p_form':p_form, 'a_form':a_form})


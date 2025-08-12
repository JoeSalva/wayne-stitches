from django.shortcuts import render, redirect
from .forms import CustomCreationForm, UpdateProfile, UpdateAddress, UpdateTopMeasurements, UpdateBottomMeasurements
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import Group


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group, _ = Group.objects.get_or_create(name='Customer')
            user.groups.add(group)
            return redirect('user:login')
    else:
        form = CustomCreationForm()
    return render(request, 'sign_up.html', {'form': form})

@login_required
@transaction.atomic
def update_profile(request):
    profile = request.user.userprofile
    address = request.user.address
    top = request.user.topmeasurement
    bottom = request.user.bottommeasurement

    if request.method == 'POST':
        p_form = UpdateProfile(request.POST, request.FILES, instance=profile)
        a_form = UpdateAddress(request.POST, instance=address)
        t_form = UpdateTopMeasurements(request.POST, instance=top)
        b_form = UpdateBottomMeasurements(request.POST, instance=bottom)

        if p_form.is_valid() and a_form.is_valid() and t_form.is_valid() and b_form.is_valid():
            p_form.save()
            a_form.save()
            t_form.save()
            b_form.save()
            return redirect('user:profile')
    else:
        p_form = UpdateProfile(instance=profile)
        a_form = UpdateAddress(instance=address)
        t_form = UpdateTopMeasurements(instance=top)
        b_form = UpdateBottomMeasurements(instance=bottom)
    return render(request, 'profile.html', {'p_form':p_form, 'a_form':a_form, 't_form':t_form, 'b_form':b_form,})
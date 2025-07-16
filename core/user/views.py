from django.shortcuts import render, redirect
from user.forms import CustomCreationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomCreationForm()
    return render(request, 'sign_up.html', {'form': form})

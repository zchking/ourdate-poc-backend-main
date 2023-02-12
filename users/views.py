# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from .models import Profile
from .forms import SignUpForm, LogInForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def profile_edit(request):
    error = False
    oPro, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=oPro)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = UpdateProfileForm(instance=oPro)
    return render(request, 'users/profile_edit.html', {'form': form, 'error': error})

def log_in(request):
    error = False
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                error = True
    else:
        form = LogInForm()

    return render(request, 'users/login.html', {'form': form, 'error': error})


def log_out(request):
    logout(request)
    return redirect(reverse('users:login'))

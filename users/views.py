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
def profile_edit(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    error = False
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance=request.user)
    return render(request, 'users/profile_edit.html', {'form': form, 'error': error})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


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

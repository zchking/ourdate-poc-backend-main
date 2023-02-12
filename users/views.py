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
def profile_edit(request, user_id):
    profile = Profile.objects.get(user=user_id)
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
            # visit accounts/profile/edit/2/ and send the screenshot to me plz
            # are you there?
            # yes http://127.0.0.1:8000/accounts/profile/edit/2/ ?
            # will it restart auto when modify code? yes, we can try runserver
            # you have dumplciate code:)  try again and show meit plz
            # it's on you local I can't visit it :)
            # do you want me to share screen or send you github with these files?
            # yes github is better, I can fork your code then push it.

            return redirect(reverse("profile_edit", kwargs={"user_id": user.id}))
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

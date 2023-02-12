# users/urls.py
from django.urls import path
from .views import profile, profile_edit, log_out

urlpatterns = [
    path('profile/', profile, name='users-profile'),
    path('profile/edit/', profile_edit, name='edit-profile'),
    path('logout/', log_out, name='logout'),
]


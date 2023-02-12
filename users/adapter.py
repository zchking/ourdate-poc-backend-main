from allauth.account.adapter import DefaultAccountAdapter
from django.shortcuts import resolve_url
from django.urls import reverse

from users.models import Profile


class AccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        try:
            profile = Profile.objects.get(user=request.user)
        except:
            return resolve_url('/accounts/profile/edit/')
        return super().get_login_redirect_url(request)

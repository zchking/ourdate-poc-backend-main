"""ourdate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic.base import TemplateView
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include(('ourdate_events.urls'), namespace='ourdate_events')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include(('users.urls', 'users'), namespace='users')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

if os.uname().sysname == 'Darwin':
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


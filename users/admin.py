# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, DateActivities, Education, Profile, Hobbies, Interests

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(Hobbies)
admin.site.register(DateActivities)
admin.site.register(Education)
admin.site.register(Interests)

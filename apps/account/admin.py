from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from apps.account import forms, models

CustomUser = get_user_model()


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    add_form = forms.UserCreationForm
    form = forms.UserChangeForm
    model = models.LeagueUser
    list_display = ('email', 'github_link')


admin.site.register(CustomUser, UserAdmin)

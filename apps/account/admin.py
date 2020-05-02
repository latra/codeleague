from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from apps.account import forms, models


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    add_form = forms.UserCreationForm
    form = forms.UserChangeForm
    model = models.LeagueUser


admin.site.register(models.LeagueUser, UserAdmin)

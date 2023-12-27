from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import *


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = CustomUser
        fields = ["email"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ["email", "password", "is_active", "is_staff", "is_superuser"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ["email", "is_active", "is_staff", "is_superuser"]
    list_filter = ["is_active", "is_staff", "is_superuser"]
    fieldsets = [
        (None, {"fields": ["password"]}),
        ("Personal info", {"fields": ["email"]}),
        ("Permissions", {"fields": ["groups", "user_permissions", "is_active", "is_staff", "is_superuser"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Profile)
admin.site.unregister(Group)

admin.site.register(ReportIssue)
admin.site.register(Ticket)
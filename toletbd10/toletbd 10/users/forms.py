from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
from .models import *

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'image', 'last_password_update']

class ReportIssueForm(forms.ModelForm):
    class Meta:
        model = ReportIssue
        fields = ['reason', 'message']
        
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"
        exclude = ["user",]




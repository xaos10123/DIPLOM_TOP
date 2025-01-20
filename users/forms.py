from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import fields

from users.models import User

class UserLoginForm(AuthenticationForm):
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
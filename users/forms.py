from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import fields

from users.models import User

class UserLoginForm(AuthenticationForm):
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('phone', 'password1', 'password2')

    def save(self, commit = ...):
        user = super().save(commit=False)
        user.username = self.cleaned_data['phone']
        if commit:
            user.save()
        return user


    # phone = forms.CharField()
    # password1 = forms.CharField()
    # password2 = forms.CharField()
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm, AuthenticationForm

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
    
class UserPasswordResetForm(PasswordResetForm):
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
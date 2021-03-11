from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError

from .models import AuthUserModel



class AuthUserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label=("Пароль"),strip=False,
        widget=forms.PasswordInput(attrs={'class': 'regform_inputs'}),
        help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField( label=("Подтверждение пароля"), strip=False,
        widget=forms.PasswordInput(attrs={'class': 'regform_inputs'}),
        help_text=("Enter the same password as before, for verification."))

    class Meta:
        model = AuthUserModel
        fields = ['email', 'username', 'first_name', 'last_name', 'phone', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'class':'regform_inputs'}),
            'username': forms.TextInput(attrs={'class':'regform_inputs'}),
            'first_name': forms.TextInput(attrs={'class':'regform_inputs'}),
            'last_name': forms.TextInput(attrs={'class':'regform_inputs'}),
            'phone': forms.TextInput(attrs={'class':'regform_inputs'}),
        }
        help_texts = {

        }
        labels = {
            'email': 'Электронная почта',
            'username': 'Логин',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'phone': 'Номер телефона',
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.EmailInput(attrs={'class': 'regform_inputs', 'autofocus': True}))
    password = forms.CharField(label="Пароль", strip=False,
                               widget=forms.PasswordInput(attrs={'class': 'regform_inputs', 'autocomplete': 'current-password'}),
                               max_length=100)
















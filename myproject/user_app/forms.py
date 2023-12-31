#forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'avatar', 'phone_number', 'country']


class CustomAuthenticationForm(AuthenticationForm):
    username = None  # Удаляем стандартное поле username
    email = forms.EmailField(label='Email', max_length=255, widget=forms.TextInput(attrs={'autofocus': True}))

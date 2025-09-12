from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Registro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)



from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# from .models import Student

class SignupForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Votre email :'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nom Utilisateur :'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe :'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe :'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')


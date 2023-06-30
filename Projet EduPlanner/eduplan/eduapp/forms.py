from django.contrib.auth.forms import PasswordResetForm
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _

class SignupForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Votre email :'}))
    
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nom Utilisateur :'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe :'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe :'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Cet e-mail est déjà utilisé.')
        return email
    

class PasswordReset(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Votre email :'}))


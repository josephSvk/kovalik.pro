from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import os
from dotenv import load_dotenv

load_dotenv()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data['email']
        allowed_domains = os.getenv('ALLOWED_EMAILS', '').split(',') # načitanie povolenych emailov 
        domain = email
        if domain not in allowed_domains:
            raise ValidationError(f"Registrácia pre doménu {domain} nie je povolená.")
        return email

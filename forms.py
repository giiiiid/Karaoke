from django import forms
from .models import Authentication

class AuthenticationForms(forms.ModelForm):
    class Meta:
        model = Authentication
        fields=[
            'username',
            'password'
        ]
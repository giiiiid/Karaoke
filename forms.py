from django import forms
from .models import Authentication, Song

class AuthenticationForms(forms.ModelForm):
    class Meta:
        model = Authentication
        fields=[
            'username',
            'password'
        ]

class AddSongForms(forms.ModelForm):
    class Meta:
        model = Song
        fields = "__all__"
from django import forms
from .models import Profile, Rating, Komentar
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gambar', 'bio']
        widgets = {
            'gambar': forms.FileInput(), # <-- Tambahkan baris ini
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['skor']
        widgets = {
            'skor': forms.HiddenInput()
        }
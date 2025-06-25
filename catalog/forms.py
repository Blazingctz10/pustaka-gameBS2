from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        # Tentukan field apa saja yang ingin ditampilkan di form registrasi
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gambar']
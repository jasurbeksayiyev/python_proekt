from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['username', 'email', 'password']
        widgets = {
                'username': forms.TextInput(attrs={'placeholder': 'Enter username'}),
                'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
                'password': forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
            }

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

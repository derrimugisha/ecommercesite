from django.contrib.auth.forms import AuthenticationForm

from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control bg-light'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control bg-light'}))
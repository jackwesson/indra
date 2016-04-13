from django import forms
from django.contrib.auth.models import User
from  django.contrib.auth import authenticate, login as django_login, logout

    
class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50, label='E-mail', widget=forms.TextInput(attrs={'placeholder': 'email address'}))
    password = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
    
class RegisterForm(forms.Form):
    name = forms.CharField(max_length=50, label='Name', widget=forms.TextInput(attrs={'placeholder': 'first & last name'}))
    email = forms.EmailField(max_length=50, label='E-mail', widget=forms.TextInput(attrs={'placeholder': 'email address'}))
    password = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    passwordConfirmation = forms.CharField(max_length=50, label='Password Confirmation', widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}))
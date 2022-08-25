from cProfile import label
from re import A
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import News


class ModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length = 256, widget=forms.TextInput(attrs = {'class': 'form__input', 'placeholder': 'Имя пользователя'}), label = 'Имя пользователя')
    first_name = forms.CharField(max_length = 256, widget=forms.TextInput(attrs = {'class': 'form__input', 'placeholder': 'Имя'}), label = 'Имя')
    last_name = forms.CharField(max_length = 256, widget=forms.TextInput(attrs = {'class': 'form__input', 'placeholder': 'Фамилия'}), label = 'Фамилия')
    email = forms.EmailField(max_length= 256, label = 'E-mail', widget=forms.EmailInput(attrs={'class': 'form__input', 'placeholder': 'E-mail'}))
    password1 = forms.CharField(max_length = 256, widget=forms.PasswordInput(attrs = {'class': 'form__input', 'placeholder': 'Пароль'}), label = 'Пароль')
    password2 = forms.CharField(max_length = 256, widget=forms.PasswordInput(attrs = {'class': 'form__input', 'placeholder': 'Повтор пароля'}), label = 'Повтор пароля')
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class AuthUserForm(AuthenticationForm):
    username = forms.CharField(max_length = 256, widget=forms.TextInput(attrs = {'class': 'form__input', 'placeholder': 'Имя пользователя'}), label = 'Имя пользователя')
    password = forms.CharField(max_length = 256, widget=forms.PasswordInput(attrs = {'class': 'form__input', 'placeholder': 'Пароль'}), label = 'Пароль')
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from .models import CustomUser


class CreateUser(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form__input'}))
    email = forms.CharField(label='Email', widget = forms.EmailInput(attrs={'class': 'form__input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form__input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form__input'}))
    birth_date = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'class': 'form__input', 'value': '17-09-2002'}))
    gender = forms.ChoiceField(label='Пол', choices = CustomUser.GENDERS, widget=forms.Select(attrs={'class': 'form__input-choice'}))
    photo = forms.ImageField(label = 'Фото профиля', widget = forms.ClearableFileInput(attrs = {'class': 'form__image-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form__input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form__input'}))
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'photo', 'gender', 'birth_date', 'password1', 'password2')


class AuthUser(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form__input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form__input'}))


class UpdateForm(UserChangeForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form__input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form__input'}))
    photo = forms.ImageField(label = 'Фото профиля', widget = forms.ClearableFileInput(attrs = {'class': 'form__image-input'}))
    email = forms.CharField(label='Email', widget = forms.EmailInput(attrs={'class': 'form__input'}))
    
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'photo', 'email')
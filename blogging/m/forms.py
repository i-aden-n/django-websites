from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import User, Blog


class UserReg(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'gender', 'phone_number', 'password1', 'password2')


class UserLogin(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserUpdate(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'image')


class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'slug', 'text', 'is_published')
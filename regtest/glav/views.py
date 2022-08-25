
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout

from .forms import CreateUser, AuthUser, UpdateForm
from .utlis import DataMixin
from .models import Post, CustomUser

CustomUser.ob
# Create your views here.
class Profile(DataMixin, LoginRequiredMixin, TemplateView):
    template_name = 'glav/profile.html'
    login_url = reverse_lazy('login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'Профиль'
        )
        context.update(c_cont)
        return context


class RegUser(DataMixin, CreateView):
    EXTRA_LINK = [
        {'url': 'login', 'title': 'Войти'}
    ]
    
    form_class = CreateUser
    template_name = 'glav/reg-auth.html'
    success_url = reverse_lazy('profile')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'Регистрация пользователя',
            headline = 'Регистрация',
            button_name = 'Зарегистрироваться',
            extra_link = self.EXTRA_LINK
        )
        context.update(c_cont)
        return context
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')


class LoginUser(DataMixin, LoginView):
    EXTRA_LINK = [
        {'url': 'register', 'title': 'Регистрация'}
    ]
    
    form_class = AuthUser
    template_name = 'glav/reg-auth.html'
    
    def get_context_data(self, **kwargs):
        print(type(self.request.user))
        print(self.request.user)
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'Авторизация пользователя',
            headline = 'Авторизация',
            button_name = 'Авторизоваться',
            extra_link = self.EXTRA_LINK
        )
        context.update(c_cont)
        return context


class Update(DataMixin, LoginRequiredMixin, UpdateView):
    form_class = UpdateForm
    template_name = 'glav/reg-auth.html'
    success_url = reverse_lazy('profile')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'Редактировать профиль',
            headline = 'Редактировать',
            button_name = 'Применить изменения'
        )
        context.update(c_cont)
        return context
    
    def get_object(self):
        return self.request.user


class Home(DataMixin, ListView):
    model = Post
    template_name = 'glav/home.html'
    context_object_name = 'posts'
    allow_empty = False
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'Главная страница'
        )
        context.update(c_cont)
        return context
    
    def get_queryset(self):
        # print(Post.objects.filter(author_id = self.request.user.pk))
        return Post.objects.filter(author_id = self.request.user.pk)


class AddPost(DataMixin, LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'glav/addpost.html'
    success_url = reverse_lazy('home')
    fields = ('title', 'text')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def logout_user(request):
    logout(request)
    return redirect('login')
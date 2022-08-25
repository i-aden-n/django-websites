from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout

from .utils import DataMixin
from .forms import UserLogin, UserReg, UserUpdate, CreateBlog
from .models import Blog, User

# Create your views here.
class Home(DataMixin, ListView):
    model = Blog
    template_name = 'm/home.html'
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context.update({
                'title': 'Home'
            })
            return context
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Blog.objects.exclude(author = self.request.user)
        return Blog.objects.all()

class Register(DataMixin, CreateView):
    form_class = UserReg
    template_name = 'm/reg-log.html'
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'User registration',
            headline = 'Registration',
            btn_msg = 'Register',
            extra_link = (
                {'url': 'login', 'name': 'LogIn'},
            )
        )
        context.update(c_cont)
        return context
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class Login(DataMixin, LoginView):
    form_class = UserLogin
    template_name = 'm/reg-log.html'
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'User authentication',
            headline = 'Authentication',
            btn_msg = 'Login',
            extra_link = (
                {'url': 'register', 'name': 'register'},
            )
        )
        context.update(c_cont)
        return context


class Profile(DataMixin, DetailView):
    model = User
    template_name = 'm/profile.html'
    context_object_name = 'user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = self.request.user.username,
        )
        context.update(c_cont)
        return context
    
    def get_object(self):
        return User.objects.get(username = self.kwargs['username'])


class Update(DataMixin, LoginRequiredMixin, UpdateView):
    form_class = UserUpdate
    template_name = 'm/reg-log.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'Update',
            headline = 'Update',
            btn_msg = 'Update',
        )
        context.update(c_cont)
        return context
    
    def get_object(self):
        return self.request.user


class AddBlog(DataMixin, LoginRequiredMixin, CreateView):
    form_class = CreateBlog
    template_name = 'm/add_blog.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'Add Blog',
        )
        context.update(c_cont)
        return context
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def logout_user(request):
    logout(request)
    return redirect('login')
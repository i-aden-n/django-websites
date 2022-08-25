from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.db.models import *
from django.urls import reverse_lazy

from .models import News, Category
from .utils import *
from .forms import ModelForm, RegisterUserForm, AuthUserForm

# Create your views here.
class Home(DataMixin, ListView):
    model = News
    template_name = 'glav/home.html'
    context_object_name = 'news'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'Главное меню'
        )
        context.update(c_cont)
        return context
    
    def get_queryset(self):
        return News.objects.order_by('-views')
    # c = Category.objects.annotate(total = Count('news')).filter(total__gt=1)
    

class ShowCategory(DataMixin, ListView):
    model = News
    template_name = 'glav/show_news.html'
    context_object_name = 'news'
    allow_empty = False
        
    def get_context_data(self, **kwargs):
        # print(self.get_queryset())
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = f'В категории {context["news"][0].cat}',
            cat_selected = context['news'][0].cat.pk
        )
        context.update(c_cont)
        return context
    
    def get_queryset(self):
        return Category.objects.get(slug = self.kwargs['cat_slug']).news_set.all()
    

class ShowItem(DataMixin, DetailView):
    model = News
    template_name = 'glav/news_detail.html'
    context_object_name = 'news'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = context['news'].title
        )
        context.update(c_cont)
        return context
    
    def get_object(self):
        object = News.objects.get(slug = self.kwargs['item_slug'])
        object.hit_view()
        return object
    

class AddNews(DataMixin, CreateView):
    model = News
    template_name = 'glav/addnews.html'
    fields = '__all__'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'Adding page'
        )
        context.update(c_cont)
        return context
    

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'glav/register.html'
    success_url = reverse_lazy('login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'Регистрация пользователя'
        )
        context.update(c_cont)
        # print(context)
        return context
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')

class LoginUser(DataMixin, LoginView):
    form_class = AuthUserForm
    template_name = "glav/login.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'Автоизация'
        )
        context.update(c_cont)
        return context
    
    def get_success_url(self):
        return reverse_lazy('profile')
    

def logout_user(request):
    logout(request)
    return redirect('home')


class Profile(DataMixin, LoginRequiredMixin, TemplateView):
    template_name = 'glav/profile.html'
    login_url = 'login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'Профиль'
        )
        context.update(c_cont)
        return context
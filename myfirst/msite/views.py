from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import News, Category

# Create your views here.

class Home(ListView):
    model = News
    template_name = 'msite/home.html'
    context_object_name = 'news'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'HOME'})
        print(context)
        return context

# def home(request):
#     context = {
#         'title': 'Home',
#     }
#     return render(request, 'msite/home.html', context = context)

class Cat(ListView):
    pass

class News(DetailView):
    pass
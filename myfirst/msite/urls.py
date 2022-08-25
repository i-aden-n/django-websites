from django.urls import path

from .views import Home, Cat, News

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('category-<slug:cat_slug>/', Cat.as_view(), name = 'cat'),
    path('category-<slug:cat_slug>/news-<slug:news_slug>', News.as_view(), name = 'news')
]
from django.urls import path

from .views import *


urlpatterns = [
    path('', Home.as_view() , name = 'home'),
    path('category-<slug:cat_slug>', ShowCategory.as_view(), name = 'show_cat'),
    path('item-<slug:item_slug>', ShowItem.as_view(), name = 'show_item'),
    path('addnews', AddNews.as_view(), name = 'addnews'),
    path('register', RegisterUser.as_view(), name = 'register'),
    path('login', LoginUser.as_view(), name = 'login'),
    path('profile', Profile.as_view(), name = 'profile'),
    path('logout', logout_user, name = 'logout')
]
from django.urls import path

from .views import *


urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('register', Register.as_view(), name = 'register'),
    path('login', Login.as_view(), name = 'login'),
    path('logout', logout_user, name = 'logout'),
    path('profile/<slug:username>', Profile.as_view(), name = 'profile'),
    path('update', Update.as_view(), name = 'update'),
    path('add_blog', AddBlog.as_view(), name = 'add_blog'),
    path('blog/<slug:blog_slug>', Home.as_view(), name = 'show_blog')
]
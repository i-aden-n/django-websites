from django.urls import path

from .views import *


urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('profile', Profile.as_view(), name = 'profile'),
    path('register', RegUser.as_view(), name = 'register'),
    path('login', LoginUser.as_view(), name = 'login'),
    path('logout', logout_user, name = 'logout_user'),
    path('update', Update.as_view(), name = 'update'),
    path('addpost', AddPost.as_view(), name = 'addpost')
]
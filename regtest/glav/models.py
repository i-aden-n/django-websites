from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
    )
    
    gender = models.CharField(max_length=1, choices=GENDERS, default='')
    birth_date = models.DateField(default='2002-09-17')
    photo = models.ImageField(upload_to = 'profile_photo/%Y/%m/%d')
    
    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField('Заголовок', max_length = 256)
    text = models.TextField('Текст', blank=True)
    published = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    author = models.ForeignKey('CustomUser', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title

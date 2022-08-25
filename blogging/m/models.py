from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    
    phone_number = models.CharField(max_length=100)
    gender = models.CharField(max_length = 1, choices = GENDERS, default='')
    about = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'profile_images/%Y/%m/%d')
    
    def get_absolute_url(self):
        return reverse('profile', kwargs = {'username': self.username})

class Blog(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField(unique = True)
    text = models.TextField(blank = True)
    photo = models.ImageField(upload_to = 'blog_images/%Y/%m/%d')
    views = models.IntegerField(default = 0)
    published = models.DateTimeField(auto_now_add = True)
    is_published = models.BooleanField(default = True)
    author = models.ForeignKey('User', on_delete = models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('show_blog', kwargs = {'blog_slug': self.slug})
    
    def __str__(self):
        return self.title
    
    def hit_view(self):
        self.views += 1
        self.save()
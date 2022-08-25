from django.db import models
from django.urls import reverse

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField(unique = True)
    text = models.TextField(blank = True)
    pre_img = models.ImageField(upload_to = 'pre_img/%Y/%m/%d')
    poster = models.ImageField(upload_to = 'poster/%Y/%m/%d')
    upload_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)
    cat = models.ForeignKey('Category', on_delete = models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('news', kwargs={'cat_slug': self.cat.slug, 'news_slug': self.slug})

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255, db_index = True, unique = True)
    slug = models.SlugField(unique = True, db_index = True)
    
    def get_absolute_url(self):
        return reverse('cat', kwargs={'cat_slug': self.slug})
    
    def __str__(self):
        return self.name
from django.db import models
from django.urls import reverse

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField(unique = True)
    text = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'news_images/%y/%m/%d')
    views = models.IntegerField(default = 0)
    upload_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)
    cat = models.ForeignKey('Category', on_delete = models.PROTECT)
    
    def hit_view(self):
        self.views += 1
        self.save()
    
    def get_ablosute_url(self):
        return reverse('show_item', kwargs = {'item_slug': self.slug})
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['upload_time']
    
    
class Category(models.Model):
    name = models.CharField(max_length = 255)
    slug = models.SlugField(unique = True, db_index = True)
    
    def get_ablsolute_url(self):
        return reverse('show_cat', kwargs = {'cat_slug': self.slug})
    
    def __str__(self):
        return self.name
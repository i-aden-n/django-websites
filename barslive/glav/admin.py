from django.contrib import admin

from .models import News, Category

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_time')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'slug')
    prepopulated_fields = {'slug': ('title', )}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'slug')
    search_fields = ('id', )
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
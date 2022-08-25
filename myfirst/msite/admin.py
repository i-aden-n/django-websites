from tkinter import NE
from django.contrib import admin

from .models import Category, News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'cat',)
    list_display_links = ('id', )
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('id', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', )
    prepopulated_fields = {'slug': ('name', )}
    search_fields = ('id', )


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
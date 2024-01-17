from django.contrib import admin
from .models import Menu, PhotoPost, Image

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'priority']

@admin.register(PhotoPost)
class PhotoPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish', 'body', 'status']
    list_filter = ['status', 'publish']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title','image')
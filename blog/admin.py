from django.contrib import admin
from .models import Menu, Post, Image, Fileupload

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'priority']

class ImageInline(admin.TabularInline):
    model = Image
    extra = 3  # Number of empty image forms to show in the admin

class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('title',)
    search_fields = ['title']

admin.site.register(Post, PostAdmin)

@admin.register(Fileupload)
class FileuploadAdmin(admin.ModelAdmin):
    list_display = ('title','slug','file')
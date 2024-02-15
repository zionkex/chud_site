from django.contrib import admin
from .models import Menu, Post, Image, Fileupload, MenuContent, Menuinfo


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'icon', 'priority']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(MenuContent)
class MenuContentAdmin(admin.ModelAdmin):
    list_display = ['menu_title', 'title', 'slug', 'icon', 'priority']


@admin.register(Menuinfo)
class MenuinfoAdmin(admin.ModelAdmin):
    list_display = ['menu_title','content_title', 'slug', 'body']
    prepopulated_fields = {'slug': ('content_title',)}


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3


class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('title',)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)


@admin.register(Fileupload)
class FileuploadAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'file')

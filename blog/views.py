from django.shortcuts import render
from .models import Menu, PhotoPost
# Create your views here.

def menu (request):
    options= Menu.objects.all()
    return render (request,'blog/base/base.html', {"options":options})

def photo_post_list(request):
    posts = PhotoPost.objects.all()
    return render(request, 'blog/photo_post.html', {'posts': posts})
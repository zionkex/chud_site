from django.shortcuts import render
from .models import Menu, PhotoPost
# Create your views here.

def menu (request):
    options= Menu.objects.all()
    return render (request,'blog/base/base.html', {"options":options})

def post_list(request):
    posts = PhotoPost.published.all()
    return render(request, 'blog/posts.html', {'posts': posts})
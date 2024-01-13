from django.shortcuts import render
from .models import Menu    
# Create your views here.

def menu (request):
    options= Menu.objects.all()
    return render (request,'blog/menulist.html', {"options":options})
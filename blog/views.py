from django.shortcuts import render
from .models import Menu    
# Create your views here.
def first (request):
    return render(request,'blog/base/base.html')
def menu (request):
    options= Menu.objects.all()
    return render (request,'blog/menulist.html', {"options":options})
from django.shortcuts import render

# Create your views here.
def first (request):
    return render(request,'blog/base/index.html')
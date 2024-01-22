from django.shortcuts import render, HttpResponse
from .models import Menu, PhotoPost
from .forms import FileuploadForm


# Create your views here.

def menu(request):
    options = Menu.objects.all()
    return render(request, 'blog/base/base.html', {"options": options})


def post_list(request):
    posts = PhotoPost.published.all()
    options = Menu.objects.all()
    context = {"options": options, 'posts': posts}
    return render(request, 'blog/posts.html', context)


def upload_file(request):
    if request.method == 'POST':
        form = FileuploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = FileuploadForm()
    context = {'form': form, }
    return render(request, 'blog/upload.html', context)


def photo_post_list(request):
    posts = PhotoPost.objects.all()
    return render(request, 'blog/photo_post.html', {'posts': posts})

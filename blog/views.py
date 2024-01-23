from django.shortcuts import render, HttpResponse,  get_object_or_404
from .models import Menu, PhotoPost, Fileupload
from .forms import FileuploadForm
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse

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


def open_pdf(request, slug):
    pdf_object = get_object_or_404(Fileupload, slug=slug)
    pdf_file = pdf_object.file
    storage = FileSystemStorage()
    pdf_path = storage.path(pdf_file.name)
    response = FileResponse(storage.open(pdf_path, 'rb'), content_type ='application/pdf')
    response["Content-Disposition"] = f"filename='{pdf_object.title}.pdf"

    return response


def post_detail():
    pass
    
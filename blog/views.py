from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.utils.encoding import escape_uri_path
from unidecode import unidecode

from .models import Post, Image, Menu, Fileupload,Menuinfo
from django.views.generic.edit import FormView
from .forms import PostForm, FileuploadForm
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.urls import reverse
from django.http import Http404


# Create your views here.

def menu(request):
    options = Menu.objects.all()
    return render(request, 'blog/base/base.html', {"options": options})


def menu_detail(request, menu_slug):
    menu_contents = Menuinfo.objects.filter(menu_title__slug=menu_slug).order_by('priority')
    if not menu_contents:
        raise Http404("No menu content found")

    options = Menu.objects.all()
    context = {'menu_contents': menu_contents, 'options': options}

    for menu_item in menu_contents:
        menu_item.url = reverse('menu_info', kwargs={'menu_slug': menu_slug, 'slug': menu_item.slug})

    return render(request, 'blog/menu_detail.html', context)


def menu_info(request, menu_slug, slug):
    options = Menu.objects.all()
    info = get_object_or_404(Menuinfo, slug=slug)
    # infos = Menuinfo.objects.filter(content_title__slug=slug)
    if not info.body:
        return redirect(info.file.url)
    else:
        context = {'info': info, 'options': options}
        return render(request, 'blog/menu_information.html', context)


class PostFormView(FormView):
    template_name = "post_form.html"
    form_class = PostForm
    success_url = "/success/"

    def form_valid(self, form):
        title = form.cleaned_data['title']
        body = form.cleaned_data['body']
        author_name = form.cleaned_data['author']
        main_image = form.cleaned_data['main_image']
        images = form.cleaned_data['images']
        author = User.objects.get(username=author_name)

        post = Post.objects.create(title=title, body=body, status=Post.Status.PUBLISHED, author=author)

        if main_image:
            Image.objects.create(post=post, image=main_image)
        for image in images:
            if image != main_image:
                Image.objects.create(post=post, image=image)

        return super().form_valid(form)


def post_list(request):
    posts = Post.published.all()
    options = Menu.objects.all()
    context = {"options": options, 'posts': posts}
    return render(request, 'blog/post/posts.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.Status.PUBLISHED)
    options = Menu.objects.all()
    return render(request,
                  'blog/post/detail.html',
                  {'post': post, 'options': options})


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


def open_pdf(request, slug):
    pdf_object = get_object_or_404(Fileupload, slug=slug)
    pdf_file = pdf_object.file
    storage = FileSystemStorage()
    pdf_path = storage.path(pdf_file.name)
    response = FileResponse(storage.open(pdf_path, 'rb'), content_type='application/pdf')
    response["Content-Disposition"] = f"filename='{pdf_object.title}'.pdf"

    return response
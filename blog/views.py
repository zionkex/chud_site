from django.shortcuts import render, HttpResponse,get_object_or_404
from .models import Post, Image, Menu,Fileupload
from .forms import FileuploadForm,PostForm
from django.views.generic.edit import FormView
from .forms import PostForm,FileuploadForm
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse    

# Create your views here.

def menu(request):
    options = Menu.objects.all()
    return render(request, 'blog/base/base.html', {"options": options})

class PostFormView(FormView):
    template_name = "post_form.html"
    form_class = PostForm
    success_url = "/success/"  # Adjust the success URL as needed

    def form_valid(self, form):
        title = form.cleaned_data['title']
        body = form.cleaned_data['body']
        main_image = form.cleaned_data['main_image']
        images = form.cleaned_data['images']
        post = Post.objects.create(title=title, body=body)

        if main_image:
            Image.objects.create(post=post, image=main_image)
        for image in images:
            if image != main_image: 
                Image.objects.create(post=post, image=image)

        return super().form_valid(form)

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post_list(request):
    posts = Post.published.all()
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

def open_pdf(request, slug):
    pdf_object = get_object_or_404(Fileupload, slug=slug)
    pdf_file = pdf_object.file
    storage = FileSystemStorage()
    pdf_path = storage.path(pdf_file.name)
    response = FileResponse(storage.open(pdf_path, 'rb'), content_type ='application/pdf')
    response["Content-Disposition"] = f"filename='{pdf_object.title}.pdf"

    return response
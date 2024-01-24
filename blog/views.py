from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import PostForm,FileuploadForm
from .models import Post, Image, Menu
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
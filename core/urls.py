"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu, name='first'),
    path('posts/', views.post_list),
<<<<<<< HEAD
    path('create_post/', views.PostFormView.as_view(), name='create_post'),
    path('home/', views.home ),
    path('files/', views.upload_file, name='upload_file')

=======
    path('photo-posts/', views.photo_post_list, name='photo_post_list'),
    path('file/', views.upload_file, name='upload_file'),
    path ('files/<slug:slug>/', views.open_pdf, name='view_pdf'),
    path('upload/', views.upload_file),
>>>>>>> 5d7547160f1e42845dc0922713855832685d4ce0
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

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
    path('', views.menu, name='menu'),
    path('posts/', views.post_list),
    path('<slug:menu_slug>/', views.menu_detail, name='menu_detail'),
    path('<slug:menu_slug>/<slug:slug>', views.menu_info, name='menu_info'),
    path('create_post/', views.PostFormView.as_view(), name='create_post'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('upload/', views.upload_file),
    # path ('files/<slug:slug>/', views.open_pdf, name='view_pdf'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

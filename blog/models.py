from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from unidecode import unidecode


class Menu(models.Model):
    title = models.CharField(max_length=20)
    slug = models.CharField(max_length=20, default=False, blank=True, null=True, )
    icon = models.CharField(max_length=50)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['priority']
        indexes = [
            models.Index(fields=['priority']),
        ]


class MenuContent(models.Model):
    menu_title = models.ForeignKey(Menu, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    icon = models.CharField(max_length=50)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        return super().save(*args, **kwargs)


class Menuinfo(models.Model):
    menu_title = models.ForeignKey(Menu, on_delete=models.CASCADE,default=1)
    content_title = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='category_images/',null=True, blank=True)
    file = models.FileField(upload_to='menu_documents/',null=True, blank=True,max_length=100)

    def __str__(self):
        return self.content_title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.content_title))
        super().save(*args, **kwargs)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset() \
            .filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, blank=True, null=True, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=None)
    body = models.TextField()
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        return super().save(*args, **kwargs)


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/')

    def __str__(self):
        return f"Image for {self.post.title}"


class Fileupload(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)
    file = models.FileField(upload_to='pdf_documents/')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

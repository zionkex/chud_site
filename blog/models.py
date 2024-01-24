from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Menu(models.Model):
    title = models.CharField(max_length=20)
    icon = models.CharField(max_length=50)
    priority = models.IntegerField(default=0)

    class Meta:
        ordering = ['priority']
        indexes = [
            models.Index(fields=['priority']),
        ]

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                      .filter(status=Post.Status.PUBLISHED)
    

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=255)
    slug = models.SlugField(default = 'none' , max_length=250,
                            unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
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
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     body = models.TextField()
#     publish = models.DateTimeField(default=timezone.now)
#     def __str__(self):
#         return self.title
#     class Meta:
#         ordering = ['-publish']
#         indexes = [
#             models.Index(fields=['-publish']),
#         ]


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/')

    def __str__(self):
        return f"Image for {self.post.title}"
 


class Fileupload(models.Model):
    title = models.CharField(max_length=255)
    slug= models.SlugField(max_length=250)
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
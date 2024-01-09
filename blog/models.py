from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=20)
    icon = models.CharField(max_length=50)
    priority = models.IntegerField(default=0)

    class Meta:
        ordering = ['priority']
        indexes = [
            models.Index(fields=['priority']),
        ]

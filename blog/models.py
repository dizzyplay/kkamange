from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']


from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


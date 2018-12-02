from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.

def main(request):
    post = Post.objects.first()
    return render(request, 'blog/main.html', {
        'post': post
    })

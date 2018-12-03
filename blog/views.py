from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


# Create your views here.

def main(request):
    qs = Post.objects.all()
    return render(request, 'blog/main.html', {
        'qs': qs
    })


def post_new(request):
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:main')
    else:
        form = PostForm()

    return render(request, 'blog/post_new.html',{
        'form':form
    })
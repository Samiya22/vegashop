from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'index.html')

def body(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'header.html', context)

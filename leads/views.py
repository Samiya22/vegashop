from multiprocessing import context
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def body(request):
    posts = Post.objects.all()
    context{
        "posts": posts
    }
    return render(request, 'header.html', context)

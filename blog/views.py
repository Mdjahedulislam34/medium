from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def about(request):
    return render(request, 'blog/about.html', {"title": "About Page"})


def home(request):
    blog_post = Post.objects.all()
    return render(request, 'blog/home.html', {"blog_post": blog_post})

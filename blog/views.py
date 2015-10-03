from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def post_list(request):
    posts=Post.objects.all()
    return render(request, 'blog/post_list.html', {"posts":posts})

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Post
from django.utils import timezone

def hello(request):
    return HttpResponse(
        'HI from me'
    )

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def post_list_dynamic(request):
    posts = Post.objects.all().order_by('published_date')
    print(posts)
    return render(request, 'blog/post_list_dynamic.html', posts)
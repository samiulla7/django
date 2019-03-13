from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from .forms import PostForm

def hello(request):
    return HttpResponse(
        'HI from me'
    )

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def post_list_dynamic(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/post_list_dynamic.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# At starting use this 
# def post_new(request):
#     form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        form_type = 'New'
    return render(request, 'blog/post_edit.html', {'form': form,'form_type':form_type})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form_type = 'Edit'
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'form_type':form_type})
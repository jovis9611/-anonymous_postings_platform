from django.shortcuts import render,redirect,get_object_or_404
from datetime import datetime,timezone
from .models import Post
from .forms import PostForm 
# Create your views here.
 
def home(request):
    post_list = Post.objects.all()
    
    return render(request, 'home.html', {
        'post_list': post_list,
    })

def post_detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.now()
            post.save()
            return redirect('trips:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('trips:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})
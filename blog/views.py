from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, CommentForm

# 1. Головна сторінка: список усіх постів
def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})

# 2. Детальна сторінка поста + логіка додавання коментаря
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', id=post.id)
    else:
        form = CommentForm()
        
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

# 3. Сторінка створення нового поста
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})
from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm


def posts(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "core/feed.html", context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)
    context = {"post": post, "comments": comments}
    return render(request, "core/post.html", context)

def createPost(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    context = {'form': form}
    return render(request, "core/post_form.html", context)


def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    context = {'form': form}
    return render(request, "core/post_form.html", context)



def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('posts')
    context = {'post': post}
    return render(request,'core/delete_post.html', context)

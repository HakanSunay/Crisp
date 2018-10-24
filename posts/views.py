from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from . import forms
from comments import forms as comment_forms
from comments.models import Comments
# Create your views here.


def posts_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/posts_list.html', context)


def posts_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
        'comments': post.comments_set.all(),
    }
    if request.method == 'POST':
        Comments.objects.create(author=request.user, post=post, content=request.POST.get('content', ''))
        return redirect('posts:detail', slug)
    return render(request, 'posts/posts_detail.html', context)


@login_required(login_url="/accounts/login/")
def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_create.html', {'form': form})

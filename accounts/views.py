from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from posts.models import Posts


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('posts:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
            logout(request)
            return redirect('posts:list')


def user_view(request, username):
    if request.method == "GET":
        # check name mangling for author__username
        # initially used .get, but that is intended for a single
        # object only, so i had to change it to .filter =)
        user_posts = Posts.objects.filter(author__username=username)
        context = {
            'posts': user_posts.values,
        }
        return render(request, 'accounts/user.html',context=context)
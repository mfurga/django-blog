from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.utils.http import is_safe_url
from django.contrib import messages
from django.urls import reverse

from .forms import SigninForm, RegisterForm, BlogSettingsForm
from aboutme.models import Contact
from .models import BlogSettings
from posts.models import Post


def users_signin(request):
    if request.user.is_authenticated:
        raise Http404

    redirect_to = request.GET.get('next', '')
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = reverse('posts:list')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Signin successfully.')
                return HttpResponseRedirect(redirect_to)

    return render(request, 'users/users_signin.html', {'form': form})


def users_register(request):
    if request.user.is_authenticated:
        raise Http404

    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'User successfully created.')
            return redirect('users:signin')

    return render(request, 'users/users_register.html', {'form': form})


@login_required
def users_dashboard(request):
    messages_list = Contact.objects.all()
    posts_list = Post.objects.all()
    users_list = User.objects.all()
    user_posts_list = Post.objects.filter(author=request.user)
    blog_settings = BlogSettings.objects.first()
    if not blog_settings:
        blog_settings = BlogSettings.objects.create(num_pages=5)

    form = BlogSettingsForm(initial={'num_pages': blog_settings.num_pages})
    if request.method == 'POST':
        form = BlogSettingsForm(request.POST)
        if form.is_valid():
            num_pages = form.cleaned_data['num_pages']
            blog_settings.num_pages = num_pages
            blog_settings.save()
            messages.success(request, 'Number of pages successfully updated.')
            return redirect('users:dashboard')

    context = {
        'messages_list': messages_list,
        'posts_list': posts_list,
        'users_list': users_list,
        'user_posts_list': user_posts_list,
        'form': form
    }
    return render(request, 'users/users_dashboard.html', context)


def users_action(request, action=None, pk=None):
    if not request.user.is_superuser:
        raise Http404
    user = get_object_or_404(User, pk=pk)
    if action == 0:
        user.is_staff = not user.is_staff
        user.save()
    elif action == 1:
        user.is_superuser = not user.is_superuser
        user.save()
    messages.success(request, 'Action successfully done.')
    return redirect('users:dashboard')


@login_required
def users_logout(request):
    logout(request)
    messages.success(request, 'Logout successfully.')
    return redirect('users:signin')

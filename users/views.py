from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils.http import is_safe_url
from django.contrib import messages
from django.urls import reverse

from .forms import SigninForm, RegisterForm, BlogSettingsForm


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

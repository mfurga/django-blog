from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q

import datetime
from .models import Post
from .forms import PostForm


def posts_list(request):
    qs = Post.objects.all()
    query = request.GET.get('q')
    if query:
        qs = qs.filter(title__contains=query)

    paginator = Paginator(qs, 3)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, 'posts/posts_list.html', {'content': content})


def posts_detail(request, slug=None):
    qs = get_object_or_404(Post, slug=slug)
    return render(request, 'posts/posts_detail.html', {'ins': qs})


@login_required
def posts_create(request):

    if request.method == 'POST':
        form = PostForm(request.POST, 
            initial={
                'author': request.user,
                'publish': datetime.date.today
            }
        )
        if form.is_valid():
            author = request.user
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            tags = form.cleaned_data['tags']
            publish = form.cleaned_data['publish']
            active = form.cleaned_data['active']

            post = Post.objects.create(
                    author=author,
                    title=title,
                    content=content,
                    tags=tags,
                    publish=publish,
                    active=active
                )

            messages.success(request, 'Post successfully added.')
            return redirect('posts:list')

    else:
        form = PostForm(initial={'author': request.user, 'publish': datetime.date.today}) 

    return render(request, 'posts/posts_create.html', {'form': form})

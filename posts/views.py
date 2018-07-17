from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Post


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

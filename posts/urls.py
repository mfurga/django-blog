from django.urls import path

from .views import posts_list, posts_detail, posts_create, posts_edit


app_name = 'posts'
urlpatterns = [
    path('', posts_list, name='list'),
    path('post/<slug:slug>', posts_detail, name='detail'),
    path('post/<slug:slug>/edit', posts_edit, name='edit'),
    path('create', posts_create, name='create')
]

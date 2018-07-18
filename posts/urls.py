from django.urls import path

from .views import posts_list, posts_detail, posts_create


app_name = 'posts'
urlpatterns = [
    path('', posts_list, name='list'),
    path('post/<slug:slug>', posts_detail, name='detail'),
    path('create', posts_create, name='create')
]

from django.urls import path

from .views import users_signin, users_register

app_name = 'users'
urlpatterns = [
    path('signin', users_signin, name='signin'),
    path('create', users_register, name='register')
]
from django.urls import path

from .views import users_signin, users_register, users_logout

app_name = 'users'
urlpatterns = [
    path('signin', users_signin, name='signin'),
    path('create', users_register, name='register'),
    path('logout', users_logout, name='logout')
]
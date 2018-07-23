from django.urls import path

from .views import aboutme_details


app_name = 'aboutme'
urlpatterns = [
    path('', aboutme_details, name='details')
]

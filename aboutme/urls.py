from django.urls import path

from .views import aboutme_details, aboutme_contact


app_name = 'aboutme'
urlpatterns = [
    path('', aboutme_details, name='details'),
    path('contact', aboutme_contact, name='contact')
]

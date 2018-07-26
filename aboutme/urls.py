from django.urls import path

from .views import aboutme_details, aboutme_contact, aboutme_delete_message


app_name = 'aboutme'
urlpatterns = [
    path('', aboutme_details, name='details'),
    path('contact', aboutme_contact, name='contact'),
    path('contact/<int:id>/delete', aboutme_delete_message, name='delete')
]

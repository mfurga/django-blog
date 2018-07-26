from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import ContactForm
from .models import Contact


def aboutme_details(request):
    return render(request, 'aboutme/aboutme_details.html', {})


def aboutme_contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            date = form.cleaned_data['date']

            Contact.objects.create(email=email, message=message, date=date)
            messages.success(request, 'Message successfully sent.')
            return redirect('posts:list')

    return render(request, 'aboutme/aboutme_contact.html', {'form': form})


def aboutme_delete_message(request, id):
    qs = get_object_or_404(Contact, id=id).delete()
    messages.success(request, 'Message successfully deleted.')
    return redirect('posts:list')

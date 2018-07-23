from django.shortcuts import render


def aboutme_details(request):
    return render(request, 'aboutme/aboutme_details.html', {})

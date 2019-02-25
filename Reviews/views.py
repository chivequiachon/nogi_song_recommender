from django.shortcuts import render

from registration.backends.simple.views import RegistrationView    


def song_review_list(request):
    return render(request, 'song_review_list.html')

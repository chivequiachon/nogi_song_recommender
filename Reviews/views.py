from django.shortcuts import render, get_object_or_404

from .models import NogizakaSong, SongReview

def song_review_list(request):
    latest_reviews = SongReview.objects.order_by('-publish_date')[:9]
    context = {'latest_reviews': latest_reviews}
    return render(request, 'song_review_list.html', context)

def song_review_detail(request, song_review_id):
    song_review = get_object_or_404(SongReview, pk=song_review_id)
    return render(request, 'song_review_detail.html', {'song_review': song_review})

def nogi_song_list(request):
    nogi_songs = NogizakaSong.objects.order_by('-name')
    context = {'nogi_songs': nogi_songs}
    return render(request, 'song_review_list.html', context)

def nogi_song_detail(request, nogi_song_id):
    nogi_song_detail = get_object_or_404(NogizakaSong, pk=nogi_song_id)
    return render(request, 'song_review_list.html', {'nogi_song': nogi_song_detail})

def user_review_list(request, username=None):
    if not username:
        username = request.user.username

    latest_reviews = SongReview.objects.filter(user_name=username).order_by('-publish_date')
    context = {'latest_reviews': latest_reviews, 'username': username}

    ## TO BE CHANGED
    return render(request, 'user_review_list.html', context)
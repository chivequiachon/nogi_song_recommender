from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import NogizakaSong, SongReview
from .forms import SongReviewForm

def song_review_list(request):
    latest_reviews = SongReview.objects.order_by('-publish_date')[:9]
    context = {'latest_reviews': latest_reviews}
    return render(request, 'song_review_list.html', context)

def song_review_detail(request, song_review_id):
    song_review = get_object_or_404(SongReview, pk=song_review_id)
    return render(request, 'song_review_detail.html', {'song_review': song_review})

def nogi_song_list(request):
    nogi_songs = NogizakaSong.objects.order_by('-romaji_title')
    context = {'nogi_songs': nogi_songs}
    return render(request, 'nogi_song_list.html', context)

def nogi_song_detail(request, nogi_song_id):
    nogi_song_detail = get_object_or_404(NogizakaSong, pk=nogi_song_id)
    return render(request, 'nogi_song_detail.html', {'nogi_song': nogi_song_detail})

def user_review_list(request, username=None):
    if not username:
        username = request.user.username

    latest_reviews = SongReview.objects.filter(user_name=username).order_by('-publish_date')
    context = {'latest_reviews': latest_reviews, 'username': username}

    return render(request, 'user_review_list.html', context)

@login_required
def add_review(request, nogi_song_id):
    song = get_object_or_404(Wine, pk=nogi_song_id)
    form = SongReviewForm(request.POST)

    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        user_name = request.user.username
        review = SongReview()
        review.song = song
        review.user_name = user_name
        review.comment = comment
        review.rating = rating
        review.pub_date = datetime.datetime.now()
        review.save()

        #update_clusters()

        return HttpResponseRedirect(reverse('song_reviews:nogi_song_detail', args=(song.id,)))

    return render(request, 'nogi_song_detail.html', {'song': song, 'form': form})
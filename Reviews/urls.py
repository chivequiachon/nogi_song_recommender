from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.song_review_list, name='song_review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.song_review_detail, name='song_review_detail'),
    # ex: /song/
    url(r'^song$', views.nogi_song_list, name='nogi_song_list'),
    # ex: /song/5/
    url(r'^song/(?P<nogi_song_id>[0-9]+)/$', views.nogi_song_detail, name='nogi_song_detail'),
    url(r'^song/(?P<nogi_song_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    # ex: /review/user - get reviews for the logged user
    url(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    url(r'^review/user/$', views.user_review_list, name='user_review_list'),
]
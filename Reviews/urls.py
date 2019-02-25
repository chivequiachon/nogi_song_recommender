from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.song_review_list, name='song_review_list'),
]
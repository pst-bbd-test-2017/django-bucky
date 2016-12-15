from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/5/  <- /music/album + /album_id
    url(
        r'^album/(?P<album_id>[0-9]+)/$',
        views.album_detail,
        name='album_detail',
    ),
    url(
        r'^album/(?P<album_id>[0-9]+)/favorite/$',
        views.favorite,
        name='favorite_song',
    ),
]

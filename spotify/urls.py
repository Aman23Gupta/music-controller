from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^get-auth-url', AuthURL),
    url(r'^redirect', spotify_callback),
    url(r'^is-authenticated', IsAuthenticated.as_view()),
    url(r'^current-song', CurrentSong.as_view())
]
from django.conf.urls import url
from .views import AuthURL, spotify_callback, IsAuthenticated

urlpatterns = [
    url(r'^get-auth-url', AuthURL),
    url(r'^redirect', spotify_callback),
    url(r'^is-authenticated', IsAuthenticated.as_view())
]
from django.conf.urls import url
from .views import index

urlpatterns = [
    url(r'^',index),
    url(r'^join/', index),
    url(r'^create/', index),
    url(r'^room/<str:roomCode>',index)
]
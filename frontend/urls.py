from django.conf.urls import url
from .views import index

app_name = 'frontend'
urlpatterns = [
    url(r'^',index,name=''),
    url(r'^join', index),
    url(r'^create', index),
    url(r'^room/<str:roomCode>',index)
]
from django.conf.urls import url
from .views import RoomView,CreateRoomView

urlpatterns = [
    url(r'^room/',RoomView.as_view()),
    url(r'^create-room',CreateRoomView.as_view())
]

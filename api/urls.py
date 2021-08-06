from django.conf.urls import url
from .views import GetRoom, RoomView,CreateRoomView

urlpatterns = [
    url(r'^room/',RoomView.as_view()),
    url(r'^create-room',CreateRoomView.as_view()),
    url(r'^get-room',GetRoom.as_view())
]

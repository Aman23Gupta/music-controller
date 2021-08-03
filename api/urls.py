from django.conf.urls import url
from .views import RoomView

urlpatterns = [
    url(r'^room/',RoomView.as_view())
]

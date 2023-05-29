from django.urls import path
from .views import DeviceConnectView, DeviceDisconnectView

urlpatterns = [
    path('connect/', DeviceConnectView.as_view()),
    path('disconnect/', DeviceDisconnectView.as_view()),
]


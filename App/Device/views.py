from http import HTTPStatus
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from App.connection_tracking import ConnectionTracking
from App.settings import CONNECTION_TRACKING_STOP_EVENT
from Logs.models import Log
from .models import *
from .forms import *


@method_decorator(csrf_exempt, name='dispatch')
class DeviceConnectView(ListView):
    def get(self, request, *args, **kwargs) -> HttpResponse:
        return HttpResponse(status=HTTPStatus.UNAUTHORIZED)
    
    def post(self, request, *args, **kwargs) -> HttpResponse:
        success, IPAddress, MACAddress = Device.Auth(self.request)
        if success:
            Device.Connect(IPAddress, MACAddress)
            Log.Info(f"Connected device from IP '{IPAddress}' and MAC '{MACAddress}'")
            ConnectionTracking(IPAddress, MACAddress)
            return HttpResponse(status=HTTPStatus.ACCEPTED)
        return HttpResponse(status=HTTPStatus.UNAUTHORIZED)
    
@method_decorator(csrf_exempt, name='dispatch')
class DeviceDisconnectView(ListView):
    def get(self, request, *args, **kwargs) -> HttpResponse:
        return HttpResponse(status=HTTPStatus.UNAUTHORIZED)
    
    def post(self, request, *args, **kwargs) -> HttpResponse:
        success, IPAddress, MACAddress = Device.Auth(self.request)
        if success:
            Device.Disconnect()
            Log.Info(f"Disconnected device from IP '{IPAddress}', MAC '{MACAddress}'")
            CONNECTION_TRACKING_STOP_EVENT.set()
            return HttpResponse(status=HTTPStatus.ACCEPTED)
        return HttpResponse(status=HTTPStatus.UNAUTHORIZED)
            
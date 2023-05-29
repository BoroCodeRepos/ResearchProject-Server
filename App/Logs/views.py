from django.shortcuts import render
from django.http import HttpResponse
from App.settings import SECRET_KEY
from Device.forms import DeviceForm
from Device.models import Device
from .models import Log

def RegisterLog(request, level, text):
    if request.method == "POST":
        form = DeviceForm(request.POST)
        key = form.cleaned_data.get("KEY")
        IPAddress = request.META.get("REMOTE_ADDR")
        if key == SECRET_KEY and Device.IsConnected(IPAddress):
            log = Log(level=level, text=text)
            log.save()
            return HttpResponse(status=200)
    return HttpResponse(status=404)

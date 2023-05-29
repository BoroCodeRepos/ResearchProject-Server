from django.db import models
from django.utils import timezone, dateformat
from django.http import HttpRequest
from App.settings import DATE_FORMAT, DEVICE_TOKEN
from .forms import DeviceForm

class Device(models.Model):
    IP = models.GenericIPAddressField()
    MAC = models.CharField(max_length=20, null=True)
    connected_time = models.DateTimeField(default=timezone.now)

    @staticmethod
    def Auth(request: HttpRequest):
        if request.method == "POST":
            form = DeviceForm(request.POST)
            if form.is_valid():
                key = form.cleaned_data.get("KEY")
                IPAddress = form.cleaned_data.get("IP")
                MACAddress = form.cleaned_data.get("MAC")
                if key == DEVICE_TOKEN:
                    return True, IPAddress, MACAddress
        return False, "", ""
    
    @staticmethod
    def Disconnect():
        cnt = Device.objects.all().count()
        if cnt > 0:
            Device.objects.all().delete()

    @staticmethod
    def Connect(IPAddress, MACAddress):
        Device.Disconnect()
        device = Device(IP=IPAddress, MAC=MACAddress)
        device.save()

    @staticmethod
    def IsConnected():
        if Device.objects.all().count() == 1:
            return True
        return False
    
    @staticmethod
    def IsConnected(IPAddress):
        if Device.objects.all().count() == 1 and Device.objects.filter(IP=IPAddress).count() == 1:
            return True
        return False

    def __str__(self):
        date = dateformat.format(self.connected_time, DATE_FORMAT)
        return f"IP: {self.IP}, connected at {date}"



from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from App.settings import SECRET_KEY
from Device.forms import DeviceForm
from Device.models import Device
from .models import Measurement

@csrf_exempt
def DeviceMeasurement(request, T, RH, p, P, O, CO2):
    if request.method == "POST":
        form = DeviceForm(request.POST)
        key = form.cleaned_data.get("KEY")
        IPAddress = request.META.get("REMOTE_ADDR")
        if key == SECRET_KEY and Device.IsConnected(IPAddress):
            measurement = Measurement(
                Temperature=T,
                Humidity=RH,
                Pressure=p,
                Power=P,
                Oxygen=O,
                CarbonDioxide=CO2
            )
            measurement.save()
            return HttpResponse(status=200)
    return HttpResponse(status=404)


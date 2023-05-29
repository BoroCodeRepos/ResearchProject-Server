from AboutUs.models import Profile, Schedule
from Device.models import Device
from Logs.models import Log
from Measurements.models import Measurement
from Publications.models import Publication
from Sources.models import Source

def default_context(request):
    ctx = {
        'publications': Publication.objects.all(),
        'sources_pub': Source.objects.filter(character="PUB"),
        'sources_oth': Source.objects.filter(character="OTH"),
    }
    return ctx
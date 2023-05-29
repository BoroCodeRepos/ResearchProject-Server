from django.db import models
from django.utils import timezone, dateformat
from App.settings import DATE_FORMAT
from Device.models import Device

class Measurement(models.Model):
    Humidity = models.CharField(max_length=20, null=False)
    CarbonDioxide = models.CharField(max_length=20, null=False)
    Oxygen = models.CharField(max_length=20, null=False)
    Temperature = models.CharField(max_length=20, null=False)
    Pressure = models.CharField(max_length=20, null=False)
    Power = models.CharField(max_length=20, null=False)
    registration_time = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        date = dateformat.format(self.registration_time, DATE_FORMAT)
        str  = f"Values: "
        str += f"Temperature: {self.Temperature} °C, "
        str += f"RH {self.Humidity}%, "
        str += f"Pressure: {self.Pressure} Pa, "
        str += f"Oxygen: {self.Oxygen}%, "
        str += f"CO2: {self.CarbonDioxide}%, "
        str += f"Power: {self.Power} W "
        str += f"-> at time {date}"
        return str


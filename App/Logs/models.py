from django.db import models
from django.utils import timezone, dateformat
from App.settings import DATE_FORMAT
from Device.models import Device

class Log(models.Model):
    LEVEL_CHOICE = [
        ("INF", "Information"),
        ("WAR", "Warning"),
        ("ERR", "Error"),
    ]
    level = models.CharField(max_length=3, choices=LEVEL_CHOICE, default="INF", null=False)
    text = models.CharField(max_length=255, null=False)
    registration_time = models.DateTimeField(default=timezone.now, null=False)

    @staticmethod
    def Info(text):
        try:
            level = "INF"
            text = str(text)
            log = Log(level=level, text=text)
            log.save()
        except:
            return False
        return True

    @staticmethod
    def Warn(text):
        try:
            level = "WAR"
            text = str(text)
            log = Log(level=level, text=text)
            log.save()
        except:
            return False
        return True

    @staticmethod
    def Error(text):
        try:
            level = "ERR"
            text = str(text)
            log = Log(level=level, text=text)
            log.save()
        except:
            return False
        return True

    def __str__(self):
        date = dateformat.format(self.registration_time, DATE_FORMAT)
        return f"[{date}] | [{self.level}] -> {self.text}"

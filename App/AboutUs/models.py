from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    POSITION_CHOICES = [
        ("CEO","Product Owner"),
        ("HWE","Hardware Engineer"),
        ("SWE","Software Engineer"),
        ("MCE","Mechanical Engineer"),
        ("BIO","Biomedical Engineer"),
        ("NSE","Network Software Engineer"),
        ("HSE","Hardware / Software Engineer"),
        ("NBS","Nobody Special"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(max_length=1000)
    position = models.CharField(max_length=5, default="NBS", choices=POSITION_CHOICES)
    image = models.ImageField(upload_to="Profiles/")

    def __str__(self):
        return f"{self.user.get_full_name()}"
    
    @staticmethod
    def get_position_name(key):
        for i in Profile.POSITION_CHOICES:
            if i[0] == key:
                return i[1]
        return ""
    
class Schedule(models.Model):
    PERCENT_CHOICES = zip(range(0,101), range(0, 101))
    COLOR_CHOICES = [
        ("bg-danger","red"),
        ("bg-warning","yellow"),
        ("bg-info","azure"),
        ("bg-success","green"),
        ("bg-primary","blue"),
        ("bg-secondary","gray"),
        #("bg-light","white"),
        ("bg-dark","dark gray"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default="bg-info")
    completion_percentage = models.IntegerField(choices=PERCENT_CHOICES)


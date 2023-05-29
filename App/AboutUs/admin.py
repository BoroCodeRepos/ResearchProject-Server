from django.contrib import admin

from .models import Profile, Schedule

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "position",)

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("user", "label", "completion_percentage",)
    list_filter = ["user"]
    ordering = ("completion_percentage", "user")

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Schedule, ScheduleAdmin)
from django import template
from AboutUs.models import Profile
register = template.Library()

@register.filter
def filter_schedule_user(schedule, user):
    return schedule.filter(user=user)

@register.filter
def filter_ceo(profile):
    return profile.filter(position="CEO")

@register.filter
def filter_contrib(profile):
    return profile.exclude(position="CEO")

@register.filter
def full_position_name(position):
    return Profile.get_position_name(position)

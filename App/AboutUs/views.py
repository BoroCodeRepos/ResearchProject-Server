from django.shortcuts import render
from Publications.models import Publication
from Sources.models import Source
from .models import Profile, Schedule
from App.default_context import default_context


def about_us(request):
    """_summary_

    :param a: _description_
    :type a: int
    :param c: _description_, defaults to [1,2]
    :type c: list, optional
    :raises AssertionError: _description_
    :return: _description_
    :rtype: _type_
    """
    context = default_context(request)
    context['profiles'] = Profile.objects.all().order_by('user__username')
    context['schedules'] = Schedule.objects.all().order_by('completion_percentage')
    return render(request, 'about_us.html', context)




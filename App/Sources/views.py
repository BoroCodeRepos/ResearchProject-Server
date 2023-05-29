from django.shortcuts import render, get_object_or_404
from Publications.models import Publication
from App.default_context import default_context

from .models import Source

def source(request, slug):
    context = default_context(request)
    context['source'] = get_object_or_404(Source, slug=slug)
    return render(request, 'source.html', context)
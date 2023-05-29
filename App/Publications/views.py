from django.shortcuts import render, get_object_or_404
from Sources.models import Source
from .models import Publication
from App.default_context import default_context

def publication(request, slug):
    context = default_context(request)
    context['publication'] = get_object_or_404(Publication, slug=slug)
    return render(request, 'publication.html', context)
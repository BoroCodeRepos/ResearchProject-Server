from django.urls import path
from . import views

urlpatterns = [
    path('source/<slug:slug>', views.source, name='source'),
]
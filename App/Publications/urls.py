from django.urls import path
from . import views

urlpatterns = [
    path('publication/<slug:slug>', views.publication, name='publication'),
]
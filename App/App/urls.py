from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static 
from AboutUs.views import about_us
from . import settings

favicon_view = RedirectView.as_view(url='/favicon.ico', permanent=True)

urlpatterns = [
    path('', include('Dashboard.urls')),
    path('', include('Publications.urls')),
    path('', include('Sources.urls')),
    path('admin', admin.site.urls, name='admin'),
    path('about-us', about_us, name='about_us'),

    path('device/', include('Device.urls')),
    path('device/', include('Measurements.urls')),
    path('device/', include('Logs.urls')),

    path('favicon.ico', favicon_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


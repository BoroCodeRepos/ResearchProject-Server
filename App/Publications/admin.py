from django.contrib import admin

from .models import Publication

class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "file",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Publication, PublicationAdmin)
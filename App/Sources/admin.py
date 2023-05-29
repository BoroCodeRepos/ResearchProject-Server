from django.contrib import admin

from .models import Source

class SourceAdmin(admin.ModelAdmin):
    list_display = ("title", "file", "url", "character")
    prepopulated_fields = {"slug": ("title",)}
    fields = [('title', 'slug'), ('file', 'url', 'character')]

admin.site.register(Source, SourceAdmin)
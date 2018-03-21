from django.contrib import admin
from .models import Location, Section

class EntryLocation(admin.ModelAdmin):
    list_display = (
        'title',
        'city',
        'country',
    )

class EntrySection(admin.ModelAdmin):
    list_display = (
        'title',
        'user',
        'section_type',
        'location',
    )

admin.site.register(Location, EntryLocation)
admin.site.register(Section, EntrySection)

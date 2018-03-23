from django.contrib import admin
from .models import Software, Hardware

class EntrySoftware(admin.ModelAdmin):
    list_display = (
        'title',
        'valid_until',
        'created_at',
    )
    save_as = True

class EntryHardware(admin.ModelAdmin):
    list_display = (
        'title',
        'model',
        'created_at',
    )
    save_as = True

admin.site.register(Software, EntrySoftware)
admin.site.register(Hardware, EntryHardware)

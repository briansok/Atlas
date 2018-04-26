from django.contrib import admin
from .models import Software, Hardware, Qrcode, Request

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

class EntryQrcode(admin.ModelAdmin):
    list_display = (
        'asset',
        'uid',
    )

class EntryRequest(admin.ModelAdmin):
    list_display = (
        'title',
        'user',
        'created_at',
    )

admin.site.register(Software, EntrySoftware)
admin.site.register(Hardware, EntryHardware)
admin.site.register(Qrcode, EntryQrcode)
admin.site.register(Request, EntryRequest)

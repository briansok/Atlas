from django.contrib import admin
from .models import Notification, Update

class EntryNotification(admin.ModelAdmin):
    list_display = (
        'title',
        'asset',
        'notification_type',
        'created_by',
        'section',
    )

class EntryUpdate(admin.ModelAdmin):
    list_display = (
        'title',
        'asset',
        'created_by',
        'section',
    )

admin.site.register(Notification, EntryNotification)
admin.site.register(Update, EntryUpdate)

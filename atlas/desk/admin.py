from django.contrib import admin
from .models import Desk

class EntryDesk(admin.ModelAdmin):
    list_display = (
        'user',
        'created_at',
    )

admin.site.register(Desk, EntryDesk)

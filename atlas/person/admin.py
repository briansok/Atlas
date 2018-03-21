from django.contrib import admin
from .models import Person

class EntryPerson(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'role',
    )

admin.site.register(Person, EntryPerson)

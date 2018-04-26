from django.contrib import admin
from .models import Person, Category


class EntryPerson(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'role',
    )


class EntryCategory(admin.ModelAdmin):
    list_display = (
        'title',
    )


admin.site.register(Person, EntryPerson)
admin.site.register(Category, EntryCategory)

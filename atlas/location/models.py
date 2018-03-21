from django.db import models
from django.conf import settings

class Location(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
        ordering = ['-created_at']

class Section(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    location = models.ForeignKey('location.Location', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    SECTION_TYPES = (
        ('room', 'Room'),
        ('area', 'Area'),
        ('desk', 'Desk'),
    )
    section_type = models.CharField(max_length=5, choices=SECTION_TYPES, default='employ')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'
        ordering = ['-created_at']

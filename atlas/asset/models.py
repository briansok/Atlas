from django.db import models
from django.conf import settings

class Asset(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    section = models.ForeignKey('location.Section', on_delete=models.CASCADE, null=True, blank=True)
    valid_until = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

class Software(Asset):
    license = models.CharField(max_length=200, null=True, blank=True)
    license_amount = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Software'
        verbose_name_plural = 'Software'
        ordering = ['-created_at']

class Hardware(Asset):
    model = models.CharField(max_length=200, null=True, blank=True)
    serial = models.CharField(max_length=200, null=True, blank=True)
    cpu = models.CharField(max_length=200, null=True, blank=True)
    ram = models.CharField(max_length=200, null=True, blank=True)
    hdd = models.CharField(max_length=200, null=True, blank=True)
    buyed_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Hardware'
        verbose_name_plural = 'Hardware'
        ordering = ['-created_at']

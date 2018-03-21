from django.db import models
from django.conf import settings

class Info(models.Model):
    title = models.CharField(max_length=200)
    asset = models.ForeignKey('asset.Asset', on_delete=models.CASCADE, null=True, blank=True)
    section = models.ForeignKey('location.Section', on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

class Notification(Info):
    NOTIFICATION_TYPES = (
        ('debug', 'Debug'),
        ('error', 'Error'),
        ('warning', 'Warning'),
        ('info', 'info'),
        ('success', 'Sucess'),
    )
    notification_type = models.CharField(max_length=7, choices=NOTIFICATION_TYPES, default='info')

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        ordering = ['-created_at']

class Update(Info):
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Update'
        verbose_name_plural = 'Updates'
        ordering = ['-created_at']


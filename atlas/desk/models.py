from django.db import models
from django.conf import settings

class Desk(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Desk'
        verbose_name_plural = 'Desks'
        ordering = ['-created_at']


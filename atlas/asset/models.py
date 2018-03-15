from django.db import models

class Software(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    license = models.CharField(max_length=200)
    license_amount = models.PostiveNumberField(blank=True)
    valid_until = models.DateField(auto_now_add=True)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Software'
        verbose_name_plural = 'Software'
        ordering = ['-created_at']

class Hardware(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    model = models.CharField(max_length=200, blank=True)
    serial = models.CharField(max_length=200, blank=True)
    cpu = models.CharField(max_length=200, blank=True)
    ram = models.CharField(max_length=200, blank=True)
    hdd = models.CharField(max_length=200, blank=True)
    buyed_at = models.DateTimeField(auto_now_add=True)
    valid_until = models.DateField(auto_now_add=True)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    #desk = models.ForeignKey('desk.Desk', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Hardware'
        verbose_name_plural = 'Hardware'
        ordering = ['-created_at']

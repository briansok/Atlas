from django.db import models
from django.conf import settings
import uuid

from model_utils.managers import InheritanceManager


class Asset(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    section = models.ForeignKey('location.Section', on_delete=models.CASCADE, null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    valid_until = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    objects = InheritanceManager()

    def __str__(self):
        return self.title

    def get_class_name(self):
        return str(self._meta)

class Software(Asset):
    license = models.CharField(max_length=200, null=True, blank=True)
    license_amount = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Software'
        verbose_name_plural = 'Software'
        ordering = ['-created_at']

    def get_edit_form(self):
        from asset.forms import AddSoftwareForm
        return AddSoftwareForm(initial={
            'title': self.title,
            'user': self.user,
            'section': self.section,
            'price': self.price,
            'valid_until': self.valid_until,
            'license': self.license,
            'license_amount': self.license_amount,
        })

    def get_post_form(self, request):
        from asset.forms import AddSoftwareForm
        return AddSoftwareForm(request)

class Hardware(Asset):
    model = models.CharField(max_length=200, null=True, blank=True)
    serial = models.CharField(max_length=200, null=True, blank=True)
    cpu = models.CharField(max_length=200, null=True, blank=True)
    ram = models.CharField(max_length=200, null=True, blank=True)
    hdd = models.CharField(max_length=200, null=True, blank=True)
    ssd = models.CharField(max_length=200, null=True, blank=True)
    bought_at = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Hardware'
        verbose_name_plural = 'Hardware'
        ordering = ['-created_at']

    def get_edit_form(self):
        from asset.forms import AddHardwareForm
        return AddHardwareForm(initial={
            'title': self.title,
            'user': self.user,
            'section': self.section,
            'price': self.price,
            'valid_until': self.valid_until,
            'model': self.model,
            'serial': self.serial,
            'cpu': self.cpu,
            'ram': self.ram,
            'hdd': self.hdd,
            'ssd': self.ssd,
            'bought_at': self.bought_at,
        })

    def get_post_form(self, request):
        from asset.forms import AddHardwareForm
        return AddHardwareForm(request)

class Qrcode(models.Model):
    asset = models.ForeignKey('asset.Asset', on_delete=models.CASCADE, null=True, blank=True)
    uid = models.CharField(max_length=50, unique=True, null=True, blank=True, default=uuid.uuid4)

    def __str__(self):
        return self.uid

    def get_qr_code_url(self, host):
        return 'https://' + host + "/assets/scan/" + self.uid



from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class Location(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    plan = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if Location.objects.exists() and not self.pk:
            raise ValidationError(_('There is can be only one location instance'))
        return super(Location, self).save(*args, **kwargs)

    def get_edit_form(self):
        from location.forms import EditLocationForm
        return EditLocationForm(initial={
            'title': self.title,
            'address': self.address,
            'zip_code': self.zip_code,
            'city': self.city,
            'country': self.country,
            'plan': self.plan,
        })

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
        ordering = ['-created_at']


class Section(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    location = models.ForeignKey('location.Location', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    plan_x = models.FloatField(null=True, blank=True)
    plan_y = models.FloatField(null=True, blank=True)

    SECTION_TYPES = (
        ('room', _('Room')),
        ('area', _('Area')),
        ('desk', _('Desk')),
    )
    section_type = models.CharField(max_length=5, choices=SECTION_TYPES, default='employ')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'
        ordering = ['title']

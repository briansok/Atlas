import datetime
from django import forms
from django.forms import SelectDateWidget
from .models import Hardware, Software, Qrcode, Request
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class DateInput(forms.DateInput):
    input_type = 'date'


class AddHardwareForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = [
            'title',
            'user',
            'section',
            'price',
            'valid_until',
            'model',
            'serial',
            'cpu',
            'ram',
            'hdd',
            'ssd',
            'bought_at',
        ]
        widgets = {
            'valid_until': DateInput(),
            'bought_at': DateInput(),
        }


class AddSoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = [
            'title',
            'user',
            'section',
            'price',
            'valid_until',
            'license',
            'license_amount',
        ]
        widgets = {
            'valid_until': DateInput(),
        }


class AddToQrcodeForm(forms.ModelForm):
    class Meta:
        model = Qrcode
        fields = [
            'asset',
        ]

    def clean_asset(self):
        asset = self.cleaned_data['asset']
        if Qrcode.objects.filter(asset=asset.id).exists():
            raise ValidationError("This asset is already linked")
        return asset


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = [
            'title',
            'description',
        ]

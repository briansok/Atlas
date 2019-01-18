from django import forms
from .models import Hardware, Software, Qrcode, Request, License
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


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
            'valid_until': forms.DateInput(attrs={'class': 'datepicker'}),
            'bought_at': forms.DateInput(attrs={'class': 'datepicker'}),
            'qr_code': forms.HiddenInput()
        }


class AddSoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = [
            'title',
            'section',
            'price',
            'valid_until',
        ]
        widgets = {
            'valid_until': forms.DateInput(attrs={'class': 'datepicker'}),
        }


class AddToQrcodeForm(forms.ModelForm):
    class Meta:
        model = Qrcode
        fields = [
            'asset',
        ]

    def __init__(self, *args, **kwargs):
        super(AddToQrcodeForm, self).__init__(*args, **kwargs)
        free_hardware_ids = []
        for qr_code in Qrcode.objects.exclude(asset=None):
            free_hardware_ids.append(qr_code.asset.id)
        self.fields['asset'].queryset = Hardware.objects.exclude(id__in=free_hardware_ids)

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


class AddLicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = [
            'user',
            'license',
            'license_amount',
        ]

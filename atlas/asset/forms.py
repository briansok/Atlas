import datetime
from django import forms
from .models import Hardware, Software, Qrcode
from django.core.exceptions import ValidationError

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
        ]

    buyed_at = forms.DateField(initial=datetime.date.today)

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

class AddToQrcodeForm(forms.ModelForm):
    class Meta:
        model = Qrcode
        fields = [
            'asset',
        ]

    def clean_asset(self):
        asset = self.cleaned_data['asset']
        if Qrcode.objects.filter(asset=asset.id).exists():
            print('bestaat')
            raise ValidationError("This asset is already linked")
        print('cleaned')
        return asset


from django import forms
from .models import Update


class AddUpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        fields = [
            'title',
            'description',
            'asset',
            'date',
            'attachment',
        ]
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'}),
        }

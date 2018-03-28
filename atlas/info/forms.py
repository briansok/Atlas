import datetime
from django import forms
from .models import Update
from django.core.exceptions import ValidationError, ObjectDoesNotExist

class AddUpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        fields = [
            'title',
            'description',
            'asset',
        ]

    date = forms.DateField(initial=datetime.date.today)

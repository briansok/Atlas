import datetime
from django import forms
from .models import Update
from django.core.exceptions import ValidationError, ObjectDoesNotExist

class DateInput(forms.DateInput):
    input_type = 'date'

class AddUpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        fields = [
            'title',
            'description',
            'asset',
            'date',
        ]
        widgets = {
            'date': DateInput(),
        }

from django import forms
from .models import Update


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

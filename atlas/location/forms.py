from django import forms
from .models import Section

class AddSectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = [
            'title',
            'location',
            'user',
            'section_type',
        ]

from django import forms
from .models import Section, Location

class AddLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            'title',
            'address',
            'zip_code',
            'city',
            'country',
            'plan',
        ]


class EditLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            'title',
            'address',
            'zip_code',
            'city',
            'country',
            'plan',
        ]


class AddSectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = [
            'title',
            'location',
            'user',
            'section_type',
        ]


class SectionPlanForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = []
    section = forms.ModelChoiceField(queryset=Section.objects.all())

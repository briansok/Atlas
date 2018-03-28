from django import forms
from person.models import Person
from location.models import Section
from django.core.exceptions import ValidationError, ObjectDoesNotExist

class AddAssetForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea())
    user = forms.ModelChoiceField(queryset=Person.objects.all(), empty_label="None")
    section = forms.ModelChoiceField(queryset=Section.objects.all(), empty_label="None")
    price = forms.IntegerField(min_value=0)

    def clean_title(self):
        title = self.cleaned_data['title']
        if Team.objects.filter(title=title).exists():
            raise ValidationError("Title is already taken")
        return title

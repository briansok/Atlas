from django import forms
from .models import Person


class EditPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'username',
            'email',
            'role',
            'category',
        ]

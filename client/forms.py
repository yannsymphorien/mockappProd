from django import forms
from . import models


class clientForm(forms.ModelForm):
    class Meta:
        model = models.client
        fields = [
            "type",
        ]

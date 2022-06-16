from django import forms
from . import models


class typeForm(forms.ModelForm):
    class Meta:
        model = models.type
        fields = [
            "nameType",
        ]

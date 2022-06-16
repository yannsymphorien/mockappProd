from django import forms
from . import models


class productForm(forms.ModelForm):
    class Meta:
        model = models.product
        fields = [
            "code",
            "nameProduct",
            "price",
            "type",
        ]

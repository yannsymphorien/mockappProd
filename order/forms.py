from django import forms
from . import models


class orderForm(forms.ModelForm):
    class Meta:
        model = models.order
        fields = [
            "product",
            "client",
        ]


class offerForm(forms.ModelForm):
    class Meta:
        model = models.offer
        fields = [
            "new_price",
            "product",
        ]

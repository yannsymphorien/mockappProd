from django.contrib import admin
from django import forms

from . import models


class productAdminForm(forms.ModelForm):

    class Meta:
        model = models.product
        fields = "__all__"


class productAdmin(admin.ModelAdmin):
    form = productAdminForm
    list_display = [
        "last_updated",
        "code",
        "nameProduct",
        "created",
        "price",
    ]
    readonly_fields = [
        "last_updated",
        "code",
        "nameProduct",
        "created",
        "price",
    ]


admin.site.register(models.product, productAdmin)

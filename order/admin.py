from django.contrib import admin
from django import forms

from . import models


class orderAdminForm(forms.ModelForm):

    class Meta:
        model = models.order
        fields = "__all__"


class orderAdmin(admin.ModelAdmin):
    form = orderAdminForm
    list_display = [
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class offerAdminForm(forms.ModelForm):

    class Meta:
        model = models.offer
        fields = "__all__"


class offerAdmin(admin.ModelAdmin):
    form = offerAdminForm
    list_display = [
        "created",
        "new_price",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "new_price",
        "last_updated",
    ]


admin.site.register(models.order, orderAdmin)
admin.site.register(models.offer, offerAdmin)

from django.contrib import admin
from django import forms

from . import models


class typeAdminForm(forms.ModelForm):

    class Meta:
        model = models.type
        fields = "__all__"


class typeAdmin(admin.ModelAdmin):
    form = typeAdminForm
    list_display = [
        "last_updated",
        "created",
        "nameType",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "nameType",
    ]


admin.site.register(models.type, typeAdmin)

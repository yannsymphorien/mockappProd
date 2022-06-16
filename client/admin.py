from django.contrib import admin
from django import forms

from . import models


class clientAdminForm(forms.ModelForm):

    class Meta:
        model = models.client
        fields = "__all__"


class clientAdmin(admin.ModelAdmin):
    form = clientAdminForm
    list_display = [
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.client, clientAdmin)


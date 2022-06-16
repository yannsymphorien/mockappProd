from rest_framework_api_key.models import AbstractAPIKey
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=128)
    active = models.BooleanField(default=True)


class OrganizationAPIKey(AbstractAPIKey):
    # ...
    class Meta(AbstractAPIKey.Meta):
        verbose_name = "Organization API key"
        verbose_name_plural = "Organization API keys"
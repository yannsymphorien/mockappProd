from django.db import models
from django.urls import reverse


class type(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    nameType = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.nameType)

    def get_absolute_url(self):
        return reverse("type_type_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("type_type_update", args=(self.pk,))

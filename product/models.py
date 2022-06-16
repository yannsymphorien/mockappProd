from django.db import models
from django.urls import reverse


class product(models.Model):

    # Relationships
    type = models.ForeignKey("type.type", on_delete=models.DO_NOTHING)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    code = models.CharField(max_length=30)
    nameProduct = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    price = models.IntegerField()

    class Meta:
        pass

    def __str__(self):
        return str(self.nameProduct)

    def get_absolute_url(self):
        return reverse("product_product_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("product_product_update", args=(self.pk,))

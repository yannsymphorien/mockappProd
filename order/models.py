from django.db import models
from django.urls import reverse


class order(models.Model):

    # Relationships
    product = models.ForeignKey("product.product", on_delete=models.DO_NOTHING)
    client = models.ForeignKey("client.client", on_delete=models.DO_NOTHING)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("order_order_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("order_order_update", args=(self.pk,))


class offer(models.Model):

    # Relationships
    product = models.ForeignKey("product.product", on_delete=models.DO_NOTHING)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    new_price = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("order_offer_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("order_offer_update", args=(self.pk,))

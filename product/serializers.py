from rest_framework import serializers

from . import models


class productSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.product
        fields = [
            "last_updated",
            "code",
            "nameProduct",
            "created",
            "price",
            "type",
        ]

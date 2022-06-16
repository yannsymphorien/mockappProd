from rest_framework import serializers

from . import models


class orderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.order
        fields = [
            "last_updated",
            "created",
        ]

class offerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.offer
        fields = [
            "created",
            "new_price",
            "last_updated",
        ]

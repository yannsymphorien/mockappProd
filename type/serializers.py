from rest_framework import serializers

from . import models


class typeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.type
        fields = [
            "last_updated",
            "created",
            "nameType",
        ]

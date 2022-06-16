from rest_framework import serializers

from . import models

from django.contrib.auth.models import User


class clientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.client
        fields = [
            "created",
            "last_updated",
            "type",
            "username",
            "password",
            "email",
            "date_of_birth",
        ]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'client']
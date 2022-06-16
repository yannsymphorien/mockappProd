from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics
from rest_framework_api_key.permissions import HasAPIKey

from . import serializers
from . import models
from .serializers import UserSerializer


class clientViewSet(viewsets.ModelViewSet):
    """ViewSet for the client class"""

    queryset = models.client.objects.all()
    serializer_class = serializers.clientSerializer
    permission_classes = []

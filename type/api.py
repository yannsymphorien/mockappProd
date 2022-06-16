from rest_framework import viewsets, permissions

from . import serializers
from . import models


class typeViewSet(viewsets.ModelViewSet):
    """ViewSet for the type class"""

    queryset = models.type.objects.all()
    serializer_class = serializers.typeSerializer
    permission_classes = [permissions.IsAuthenticated]

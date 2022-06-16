from rest_framework import viewsets, permissions

from . import serializers
from . import models


class productViewSet(viewsets.ModelViewSet):
    """ViewSet for the product class"""

    queryset = models.product.objects.all()
    serializer_class = serializers.productSerializer
    permission_classes = [permissions.IsAuthenticated]

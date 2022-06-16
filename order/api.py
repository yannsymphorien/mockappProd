from rest_framework import viewsets, permissions

from . import serializers
from . import models


class orderViewSet(viewsets.ModelViewSet):
    """ViewSet for the order class"""

    queryset = models.order.objects.all()
    serializer_class = serializers.orderSerializer
    permission_classes = [permissions.IsAuthenticated]


class offerViewSet(viewsets.ModelViewSet):
    """ViewSet for the offer class"""

    queryset = models.offer.objects.all()
    serializer_class = serializers.offerSerializer
    permission_classes = [permissions.IsAuthenticated]

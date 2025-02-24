from rest_framework import viewsets
from .models import UserStats, OrderStats, ProposalStats
from .serializers import UserStatsSerializer, OrderStatsSerializer, ProposalStatsSerializer

class UserStatsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserStats.objects.all()
    serializer_class = UserStatsSerializer

class OrderStatsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OrderStats.objects.all()
    serializer_class = OrderStatsSerializer

class ProposalStatsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProposalStats.objects.all()
    serializer_class = ProposalStatsSerializer

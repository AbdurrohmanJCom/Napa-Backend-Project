from rest_framework import serializers
from .models import UserStats, OrderStats, ProposalStats

class UserStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStats
        fields = '__all__'

class OrderStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStats
        fields = '__all__'

class ProposalStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposalStats
        fields = '__all__'

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserStatsViewSet, OrderStatsViewSet, ProposalStatsViewSet

router = DefaultRouter()
router.register(r'user-stats', UserStatsViewSet)
router.register(r'order-stats', OrderStatsViewSet)
router.register(r'proposal-stats', ProposalStatsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FinancialGoalViewSet, TransactionViewSet, InvestmentViewSet

router = DefaultRouter()
router.register(r'goals', FinancialGoalViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'investments', InvestmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

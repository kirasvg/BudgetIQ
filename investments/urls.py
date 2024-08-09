from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvestmentRecommendationViewSet, PortfolioAnalysisViewSet
router = DefaultRouter()
router.register(r'investment-recommendations', InvestmentRecommendationViewSet)
router.register(r'portfolio-analyses', PortfolioAnalysisViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
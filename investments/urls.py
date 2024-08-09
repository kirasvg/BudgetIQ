from rest_framework.routers import DefaultRouter
from .views import InvestmentViewSet,InvestmentRecommendationView,PortfolioAnalysisView
from django.urls import path

router = DefaultRouter()
router.register(r'investments', InvestmentViewSet, basename='investment')

urlpatterns = router.urls

urlpatterns += [
    path('investments/recommendations/', InvestmentRecommendationView.as_view(), name='investment-recommendations'),
    path('investments/portfolio/', PortfolioAnalysisView.as_view(), name='portfolio-analysis'),
]

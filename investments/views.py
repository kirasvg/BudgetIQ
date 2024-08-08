from rest_framework import viewsets
from .models import InvestmentRecommendation,PortfolioAnalysis
from .serializers import InvestmentRecommendationSerializer, PortfolioAnalysisSerializer
class InvestmentRecommendationViewSet(viewsets.ModelViewSet):
    queryset = InvestmentRecommendation.objects.all()
    serializer_class = InvestmentRecommendationSerializer

class PortfolioAnalysisViewSet(viewsets.ModelViewSet):
    queryset = PortfolioAnalysis.objects.all()
    serializer_class = PortfolioAnalysisSerializer

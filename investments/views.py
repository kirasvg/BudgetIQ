from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Investment
from .serializers import InvestmentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from .ai import AIInvestmentAdvisor
class InvestmentViewSet(viewsets.ModelViewSet):
    serializer_class = InvestmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Investment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class InvestmentRecommendationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        advisor = AIInvestmentAdvisor()
        recommendation = advisor.recommend(request.user)
        return Response(recommendation)

class PortfolioAnalysisView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        summary = Investment.portfolio_summary(request.user)
        return Response(summary)

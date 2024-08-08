from rest_framework import serializers
from .models import InvestmentRecommendation, PortfolioAnalysis

class InvestmentRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentRecommendation
        fields = '__all__'

class PortfolioAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioAnalysis
        fields = '__all__'

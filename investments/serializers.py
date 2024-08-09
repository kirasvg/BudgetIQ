from rest_framework import serializers
from .models import Investment

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = ['id', 'name', 'amount_invested', 'current_value', 'risk_level', 'purchase_date']

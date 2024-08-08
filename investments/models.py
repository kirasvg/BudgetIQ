from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class InvestmentRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation = models.TextField()
    risk_level = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    created_at = models.DateTimeField(auto_now_add=True)

class PortfolioAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    analysis = models.TextField()
    diversification_suggestions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

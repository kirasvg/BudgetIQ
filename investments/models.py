from django.db import models
from django.contrib.auth.models import User

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount_invested = models.DecimalField(max_digits=10, decimal_places=2)
    current_value = models.DecimalField(max_digits=10, decimal_places=2)
    risk_level = models.CharField(max_length=50)
    purchase_date = models.DateField()

    def __str__(self):
        return self.name
    
    def portfolio_summary(user):
        investments = Investment.objects.filter(user=user)
        total_investment = investments.aggregate(models.Sum('amount_invested'))['amount_invested__sum'] or 0
        average_risk = investments.aggregate(models.Avg('risk_level'))['risk_level__avg'] or "Medium"
        return {
            "total_investment": total_investment,
            "average_risk": average_risk,
            "diversification": "Moderate",  # This could be calculated more precisely
        }

from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    
    def is_overrun(self):
        total_expense = self.expenses.aggregate(total=models.Sum('amount'))['total'] or 0
        return total_expense > self.total_amount

    def send_alert_if_overrun(self):
        if self.is_overrun():
            send_mail(
                'Budget Overrun Alert',
                f'Your budget {self.name} is overrun!',
                'from@example.com',
                [self.user.email],
                fail_silently=False,
            )

class Expense(models.Model):
    budget = models.ForeignKey(Budget, related_name='expenses', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.category}: {self.amount}"

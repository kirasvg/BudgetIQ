from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BudgetViewSet, ExpenseViewSet,BudgetReportView

router = DefaultRouter()
router.register(r'budgets', BudgetViewSet)
router.register(r'expenses', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('budget/report/', BudgetReportView.as_view(), name='budget-report'),
]

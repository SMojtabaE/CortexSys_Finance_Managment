from django.urls import path
from .views import BudgetsListCreateView, BudgetsRetrieveUpdateDestroyView



urlpatterns = [
        path('', BudgetsListCreateView.as_view(), name='budget-list-create'),
        path('<int:pk>/', BudgetsRetrieveUpdateDestroyView.as_view(), name='budget-detail'),
    ]
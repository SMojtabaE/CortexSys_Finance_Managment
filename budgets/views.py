from rest_framework import generics
from .models import Budgets
from .serializers import BudgetsSerializer

class BudgetsListCreateView(generics.ListCreateAPIView):
        queryset = Budgets.objects.all()
        serializer_class = BudgetsSerializer

class BudgetsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Budgets.objects.all()
        serializer_class = BudgetsSerializer
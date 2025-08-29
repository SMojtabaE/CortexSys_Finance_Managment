from rest_framework import generics
from .models import Budgets
from .serializers import BudgetsSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

class BudgetsListCreateView(generics.ListCreateAPIView):
        queryset = Budgets.objects.all()
        serializer_class = BudgetsSerializer

        permission_classes = [IsAuthenticated, IsOwner]

        def get_queryset(self):
                queryset = Budgets.objects.filter(user=self.request.user)  
                return queryset
        def perform_create(self, serializer):
                serializer.save(user=self.request.user)

class BudgetsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Budgets.objects.all()
        serializer_class = BudgetsSerializer

        permission_classes = [IsAuthenticated, IsOwner]
from rest_framework import generics
from .models import Budgets
from .serializers import BudgetsSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

class BudgetsListCreateView(generics.ListCreateAPIView):
        # GET and POST 
        # this view gets a list of budgets,and also can create a new budget
        
        queryset = Budgets.objects.all()
        serializer_class = BudgetsSerializer

        permission_classes = [IsAuthenticated, IsOwner]

        def get_queryset(self):
                # Limite the search for only getting the budgets that the user have made
                queryset = Budgets.objects.filter(user=self.request.user)  
                return queryset
        def perform_create(self, serializer):
                # add user to serializer
                serializer.save(user=self.request.user)

class BudgetsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
        # GET PUT PACHT DELETE
        # can get detail of a budget,update and delete the budget using its PK

        queryset = Budgets.objects.all()
        serializer_class = BudgetsSerializer

        permission_classes = [IsAuthenticated, IsOwner]
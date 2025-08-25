from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

class TransactionListCreateView(generics.ListCreateAPIView):
        queryset = Transaction.objects.all()
        serializer_class = TransactionSerializer
        permission_classes = [IsAuthenticated, IsOwner]

        def get_queryset(self):
                queryset = Transaction.objects.filter(user=self.request.user)  
                return queryset
        

class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Transaction.objects.all()
        serializer_class = TransactionSerializer

        permission_classes = [IsAuthenticated, IsOwner]
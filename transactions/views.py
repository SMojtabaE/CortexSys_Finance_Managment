from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner


class TransactionListCreateView(generics.ListCreateAPIView):
        # GET and POST 
        # this view gets a list of transactions,and also can create a new transaction
        
         
        queryset = Transaction.objects.all()
        serializer_class = TransactionSerializer
        permission_classes = [IsAuthenticated, IsOwner]

        def get_queryset(self):
                # Limite the search for only getting the transactions that the user have made

                queryset = Transaction.objects.filter(user=self.request.user)  
                return queryset

        def perform_create(self, serializer):
                # add user to serializer
                serializer.save(user=self.request.user)
        

class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
        # GET PUT PACHT DELETE
        # can get detail of a transaction,update and delete the transaction using its PK

        queryset = Transaction.objects.all()
        serializer_class = TransactionSerializer

        permission_classes = [IsAuthenticated, IsOwner]
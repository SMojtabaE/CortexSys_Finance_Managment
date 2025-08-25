from django.db import models

from django.contrib.auth.models import User


class Transaction(models.Model):
    
    class TypeChoices(models.TextChoices):
        Income = 'Income'
        Expense = 'Expense'

    title = models.CharField(max_length=50)
    amount = models.FloatField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    note = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    typem = models.CharField(
            max_length=10,
            choices=TypeChoices.choices,
            default=TypeChoices.Expense
        )
        
    class Meta:
        ordering = ['-date']

        
    def __str__(self):
        return self.title
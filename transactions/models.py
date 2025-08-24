from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Transaction(models.Model):
    
    class TypeChoices(models.TextChoices):
        Income = 'Income'
        Expense = 'Expense'

    title = models.CharField(max_length=50)
    amount = models.FloatField()
    status = models.CharField(
        max_length=10,
        choices=TypeChoices.choices,
        default=TypeChoices.Expense
    )
    date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-date']

        
    def __str__(self):
        return self.title
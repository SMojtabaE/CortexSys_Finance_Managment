from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Budgets(models.Model):
    
    title = models.CharField(max_length=50)
    total_amount = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    

    @property
    def Is_Active(self):
        return self.start_date < timezone.now().date() < self.end_date

    class Meta:
        ordering = ['-end_date']

        
    def __str__(self):
        return self.title
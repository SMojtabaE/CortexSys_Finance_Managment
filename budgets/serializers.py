from rest_framework import serializers
from .models import Budgets

class BudgetsSerializer(serializers.ModelSerializer):

    # start_date = serializers.DateField(format="%Y-%m-%d")
    # end_date = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        model = Budgets
        fields = (['title', 'total_amount','start_date','end_date','Is_Active','user'])
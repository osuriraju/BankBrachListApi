from rest_framework import serializers
from .models import BanksList

class BankListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BanksList
        fields = '__all__'


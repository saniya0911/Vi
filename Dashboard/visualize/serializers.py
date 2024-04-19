from rest_framework import serializers
from .models import MarketReport

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketReport
        fields = '__all__'
from rest_framework import serializers
from .models import ApiResponse

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiResponse
        fields = '__all__'
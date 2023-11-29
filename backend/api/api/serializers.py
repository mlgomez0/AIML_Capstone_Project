from rest_framework import serializers
from .models import ApiResponse
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError

UserModel = get_user_model()

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiResponse
        fields = '__all__'

class UserLoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()
	##
	def check_user(self, clean_data):
		user = authenticate(username=clean_data['username'], password=clean_data['password'])
		if not user:
			raise ValidationError('user not found')
		return user

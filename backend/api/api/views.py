from rest_framework.response import Response
from django.http import JsonResponse

from .models import ApiResponse, ChatHistory
from .modules_ai.llm_talker import LlmTalker
from .serializers import ItemSerializer
from django.contrib.auth import login, logout
from .serializers import UserLoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import status


conversations = {}

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()  # Empty or include any other desired authentication classes

    def post(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)

            # Create or retrieve a token for the authenticated user
            token, created = Token.objects.get_or_create(user=user)

            # Include token in response
            return Response({
                'token': token.key,
                'user_data': serializer.data
            }, status=status.HTTP_200_OK)
		
class ChatHistoryStore(APIView):
	authentication_classes = [SessionAuthentication, TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]
	##
	def get(self, request):
		try:
			record = ChatHistory.objects.get(username=request.user.username)
		except ChatHistory.DoesNotExist:
			return JsonResponse({'error': 'Record not found'}, status=404)
		response_data = {
			'username': record.username,
			'chat': record.text_field,
    	}
		return JsonResponse(response_data, status=status.HTTP_200_OK)

	def post(self, request):
		data = request.data
		ChatHistory.objects.update_or_create(
                username=request.user.username,
                defaults={'text_field': data['chat']}
            )
		return Response(status=status.HTTP_200_OK)
	
class ChatRatingHistory(APIView):

	authentication_classes = [SessionAuthentication, TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]

	def get(self, request):
		try:
			record = ChatHistory.objects.get(username=request.user.username)
		except ChatHistory.DoesNotExist:
			return JsonResponse({'error': 'Record not found'}, status=404)
		response_data = {
			'username': record.username,
			'rating': record.rating,
    	}
		return JsonResponse(response_data, status=status.HTTP_200_OK)
	
	def post(self, request):
		data = request.data
		ChatHistory.objects.update_or_create(
                username=request.user.username,
                defaults={'rating': data['rating']}
            )
		return Response(status=status.HTTP_200_OK)


class UserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)
	
class ChatView(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	##

	def get(self, request):
		return Response(status=status.HTTP_200_OK)
	def post(self, request):
		data = request.data
		talker = LlmTalker()
		user_input = data["q"]
		answer = talker.chat(user_input)
		response = ApiResponse()
		response.text = answer
		serializer = ItemSerializer(response, many=False)
		return Response({'chat': serializer.data}, status=status.HTTP_200_OK)
	

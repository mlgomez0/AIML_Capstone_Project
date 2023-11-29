from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ApiResponse
from .modules_ai.llm_talker import LlmTalker
from .serializers import ItemSerializer
from django.contrib.auth import login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserLoginSerializer
from rest_framework import permissions, status

conversations = {}

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@api_view(['POST'])
def predict(request):

    # Get client IP
    client_ip = get_client_ip(request)
    print('REQUEST:', client_ip)
    
    talker = LlmTalker()
    user_input = request.GET.dict()["q"]

    answer = talker.chat(user_input)
    response = ApiResponse();
    response.text = answer

    serializer = ItemSerializer(response, many=False)
    return Response(serializer.data)

class UserLogin(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = (SessionAuthentication,)
	##
	def post(self, request):
		data = request.data
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.check_user(data)
			login(request, user)
			return Response(serializer.data, status=status.HTTP_200_OK)


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
	

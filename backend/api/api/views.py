from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ApiResponse
from .modules_ai.llm_talker import LlmTalker
from .serializers import ItemSerializer

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
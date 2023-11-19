from rest_framework.decorators import api_view
from rest_framework.response import Response

from .llm import LargeLanguageModel
from .models import ApiResponse
from .modules_ai.llm_talker import LlmTalker
from .serializers import ItemSerializer

app = LargeLanguageModel('./../../data')
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

    user_history = conversations.get(client_ip, []);
    
    #talker = LlmTalker()
    user_input = request.GET.dict()["q"]

    # Generate a response from model
    resp, conversation = app.create_conversation(user_input, user_history)

    # Return response
    #answer, _ = talker.chat(q) # pending to fix 
    response = ApiResponse();
    response.text = conversation[0][1]
    serializer = ItemSerializer(response, many=False)
    return Response(serializer.data)
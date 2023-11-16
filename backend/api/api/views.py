from rest_framework.decorators import api_view
from rest_framework.response import Response
from .modules_ai.llm_talker import LlmTalker


from .models import ApiResponse
from .serializers import ItemSerializer


@api_view(['POST'])
def predict(request):

    talker = LlmTalker()
    q = request.GET.dict()["q"]
    #answer, _ = talker.chat(q) # pending to fix 
    response = ApiResponse();
    response.text = f'Hello {q}'
    serializer = ItemSerializer(response, many=False)
    return Response(serializer.data)
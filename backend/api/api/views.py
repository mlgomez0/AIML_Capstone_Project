from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ApiResponse
from .serializers import ItemSerializer


@api_view(['POST'])
def predict(request):

    # Get the parameter named 'q' from the request
    q = request.GET.dict()["q"]
    response = ApiResponse();
    response.text = f'Hello {q}'
    serializer = ItemSerializer(response, many=False)
    return Response(serializer.data)
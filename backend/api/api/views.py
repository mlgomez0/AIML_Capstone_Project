from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def item_list(request):
    items = [
        Item(first_name='Peter', last_name='Thomas'),
    ]
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ApiResponse
from .serializers import ItemSerializer
from .llm import LlModel

llm = LlModel

model = LlModel()

@api_view(['POST'])
def predict(request):

    # Get the parameter named 'q' from the request
    q = request.GET.dict()["q"]

    # Generate a response from model
    inputs = model.tokenizer.encode(q, return_tensors='pt')
    
    # Generate text using the model
    outputs = model.generate(inputs, stop_token_ids=stop_token_ids)
    generated_text = model.tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Return response
    response = ApiResponse();
    response.text = generated_text
    serializer = ItemSerializer(response, many=False)
    return Response(serializer.data)
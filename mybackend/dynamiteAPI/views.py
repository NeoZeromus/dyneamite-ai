from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import MessageSerializer

@api_view(['GET'])
def hello_world(request):
    message = "Hello, World! This is your Django REST Framework API."
    return Response({"message": message})

@api_view(['POST'])
def echo(request):
    res = "PONG"
    if request.method == 'POST':
        # Check if the 'message' key is present in the request data
        if 'message' in request.data:
            # Retrieve the message from the request data
            message = request.data['message']
            return Response({"message": res}, status=status.HTTP_200_OK)
        else:
            # If 'message' key is not present in request data
            return Response({"error": "Message key not found in request data"}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def create_post(request):
    if request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

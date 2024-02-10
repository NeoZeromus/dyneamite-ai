from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from nltk.tokenize import word_tokenize

from .serializers import MessageSerializer
from .serializers import APISerializer

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

conjunctions_and_connectors = [
    "and",
    "but",
    "or",
    "nor",
    "yet",
    "so",
    "for",
    "because",
    "since",
    "although",
    "though",
    "while",
    "whereas",
    "unless",
    "until",
    "therefore",
    "hence",
    "thus",
    "furthermore",
    "moreover",
    "an",
    "a",
    "of",
    "the",
    "that"
]

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
        requestData = request.data
        
        message = request.data['message']
        
        tokens = word_tokenize(message)
        
        tokens = [word for word in tokens if word not in conjunctions_and_connectors]
        
        requestData["tokens"] = tokens
        
        serializer = MessageSerializer(data=requestData)
        
        if serializer.is_valid():
            serializer.save()
            
            query = search_rows(tokens)
            
            print(query)
            
            return Response(query, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def create_API_object(request):
    if request.method == 'POST':
        listOfAPIs = request.data['apis']
        
        for api in listOfAPIs:
            
            apiData = {"api": api}
            
            apiSerializer = APISerializer(data=apiData)
            
            print(apiSerializer)
            
            if apiSerializer.is_valid():
                apiSerializer.save()
            else:
                return Response(apiSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(listOfAPIs, status=status.HTTP_201_CREATED)
    
from django.http import JsonResponse
from .models import API

def search_rows(request):
    # # Get the words to search for from the request
    # words_to_search = request.GET.get('words', '').split()

    # Query the database for rows containing any of the words
    # if request:
    #     queryset = API.objects.filter(api__icontains=request)
    #     for word in request:
    #         queryset = queryset.filter(api__icontains=word)
    # else:
    #     queryset = API.objects.none()  # Return an empty queryset if no words provided
    
    queryset = API.objects.all()
    for word in request:
        queryset = queryset.filter(api__icontains=word)

    # Serialize the queryset and return as JSON response
    data = [{'id': row.id, 'api': row.api} for row in queryset]

    return data

                
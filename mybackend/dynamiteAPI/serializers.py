from rest_framework import serializers

from .models import Message
from .models import API

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        app_label = 'dynamiteAPI'
        model = Message
        fields = ['message', 'tokens', 'created_at']
        
class APISerializer(serializers.ModelSerializer):
    class Meta:
        app_label = 'dynamiteAPI'
        model = API
        fields = ['api', 'created_at']
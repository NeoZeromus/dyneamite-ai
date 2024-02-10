from rest_framework import serializers

from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        app_label = 'dynamiteAPI'
        model = Message
        fields = ['message', 'tokens', 'created_at']
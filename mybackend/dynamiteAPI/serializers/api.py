from rest_framework import serializers

from models import Api

class ApiModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = ["message", "created_at"]
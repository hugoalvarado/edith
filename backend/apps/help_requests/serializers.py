from rest_framework import serializers
from .models import HelpRequest


class HelpRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = HelpRequest
        fields = ['description', 'completed', 'created_at']

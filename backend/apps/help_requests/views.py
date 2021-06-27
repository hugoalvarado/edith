from django.shortcuts import render
from rest_framework import viewsets
from .models import HelpRequest
from .serializers import HelpRequestSerializer


class HelpRequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows help requests to be viewed or edited.
    """
    queryset = HelpRequest.objects.all()
    serializer_class = HelpRequestSerializer

from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework import permissions
from .models import Project, Example
from .serializers import ProjectSerializer, ExampleSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Projects to be viewed or edited.
    """
    queryset = Project.objects.all().order_by('-created_on')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExampleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Examples to be viewed or edited.
    """
    queryset = Example.objects.all().order_by('-created_on')
    serializer_class = ExampleSerializer
    permission_classes = [permissions.IsAuthenticated]

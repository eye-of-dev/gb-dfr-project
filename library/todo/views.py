from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from todo.models import Projects
from todo.serializers import ProjectsModelSerializer


class ProjectsModelViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsModelSerializer

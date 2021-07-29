from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework import generics, permissions

# Create your views here.
# CBV (Class Base Views)

# List --> GET data
# Create --> POST data
# Retrieve --> GET data (id)
# Update --> PUT data (id)
# Destroy --> DELETE data (id)


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


    # only ann authenticatied user can access this API
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


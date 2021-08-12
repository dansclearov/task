from rest_framework import viewsets

from todo import models
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer
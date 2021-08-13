from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as df_filters

from todo import models
from .serializers import TodoSerializer
from .filters import TodoDateTimeFilter


class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, df_filters.DjangoFilterBackend]
    filterset_class = TodoDateTimeFilter
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'description', 'favourite', 'created_at', 'updated_at']

    @action(detail=True)
    def favourite_toggle(self, request, pk=None):
        todo = self.retrieve(request, pk)
        request.data["favourite"] = not todo.data["favourite"]
        return self.partial_update(request, pk)
    
    @action(detail=False)
    def list_favourite(self, request):
        queryset = self.queryset.filter(favourite=True)
        serializer = self.serializer_class(queryset, many=True, context={ "request": request })
        return Response(serializer.data)
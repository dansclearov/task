from django_filters import rest_framework as django_filters

from todo import models


class TodoDateTimeFilter(django_filters.FilterSet):
    class Meta:
        model = models.Todo
        fields = {
            'created_at': ['lte', 'gte', 'lt', 'gt'],
            'updated_at': ['lte', 'gte', 'lt', 'gt'],
        }
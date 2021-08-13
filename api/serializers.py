from rest_framework import serializers
from todo import models


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = (
            'url',
            'title',
            'description',
            'favourite',
            'created_at',
            'updated_at'
        )
        model = models.Todo
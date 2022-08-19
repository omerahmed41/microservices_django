from rest_framework import serializers
from todoList.models import TodoItem


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id', 'content', 'priority', 'flag', 'expireDate', 'createDate')



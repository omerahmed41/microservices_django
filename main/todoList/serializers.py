from rest_framework import serializers
from todoList.models import TodoItem


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = TodoItem
        fields = ('id', 'owner', 'content', 'priority', 'flag', 'expireDate', 'created_at')


class TodoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id', 'content', 'priority', 'flag')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return TodoItem.objects.create(**validated_data)

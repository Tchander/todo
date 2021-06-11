from rest_framework import serializers
from .models import TodoCategory, TodoList


class TodoListSerializer(serializers.ModelSerializer):
    """
    Сериализатор списка todos
    """

    class Meta:
        model = TodoList
        exclude = ('category', )


class TodoCategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор списка категорий
    """
    todos = serializers.SerializerMethodField()

    @staticmethod
    def get_todos(obj):
        return TodoListSerializer(TodoList.objects.filter(category=obj.id), many=True).data

    class Meta:
        model = TodoCategory
        fields = '__all__'

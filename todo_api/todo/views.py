from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from .models import TodoCategory, TodoList
from .serializers import TodoCategorySerializer, TodoListSerializer


class TodoListView(APIView):
    """
    Вывод списка всех todos
    """

    @staticmethod
    def get(request):
        todo_category = TodoCategorySerializer(TodoCategory.objects.all(), many=True).data
        return Response(todo_category)

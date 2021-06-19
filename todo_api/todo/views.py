from rest_framework.response import Response

from .models import TodoCategory, TodoList
from .serializers import TodoCategorySerializer, TodoListSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import ViewSet


class TodoListView(ViewSet):
    """
    Вывод списка всех todos
    """

    @staticmethod
    def list(request):
        todo_category = TodoCategorySerializer(TodoCategory.objects.all(), many=True).data
        return Response(todo_category)

    @staticmethod
    def partial_update(request, pk):
        todo = TodoList.objects.get(pk=pk)
        serializer = TodoListSerializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



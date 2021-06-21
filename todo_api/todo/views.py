from rest_framework.response import Response

from .models import TodoCategory, TodoList
from .serializers import TodoCategorySerializer, TodoListSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import ViewSet


class TodoListView(ViewSet, GenericAPIView):
    """
    Вывод списка всех todos
    """
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    @staticmethod
    def list(request):
        todo_category = TodoCategorySerializer(TodoCategory.objects.all(), many=True).data
        return Response(todo_category)

    @staticmethod
    def create(request, *args, **kwargs):
        print(request.data)
        title = request.data.get('title')
        text = request.data.get('text')
        category, _ = TodoCategory.objects.get_or_create(title=title)
        data = {
            'text': text,
            'category': category
        }
        serializer = TodoListSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.create(validated_data=data)
        return Response(serializer.data)

    def partial_update(self, request, pk):
        # todo = self.get_queryset().get(pk=pk)
        todo = self.get_object()
        serializer = self.get_serializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @staticmethod
    def destroy(request, pk):
        todo = TodoList.objects.get(pk=pk)
        todo.delete()
        return Response(status=200)



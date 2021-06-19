# from django.urls import path
#
# from todo.views import TodoListView
#
# urlpatterns = [
#     path('todos/', TodoListView.as_view()),
#     path('todos/<int:cardId>/todo/<int:todoId>', TodoListView.as_view())
# ]

from django.urls import path
from django.urls import include
from rest_framework.routers import SimpleRouter
from todo.views import TodoListView


router = SimpleRouter()

router.register('todos', TodoListView, basename='todos')

urlpatterns = router.urls

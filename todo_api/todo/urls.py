from django.urls import path

from todo.views import TodoListView

urlpatterns = [
    path('todos/', TodoListView.as_view())
]
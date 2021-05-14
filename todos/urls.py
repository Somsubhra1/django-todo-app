from django.urls import path
from .views import TodoListView, TodoDeleteView, TodoCreateView

app_name = "todos"

urlpatterns = [
    path("", TodoListView.as_view(), name="home"),
    path("todos/create/", TodoCreateView.as_view(), name="todo-create"),
    path("todos/<int:pk>/delete", TodoDeleteView.as_view(), name="todo-delete"),
]

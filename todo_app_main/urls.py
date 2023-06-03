from django.urls import path
from .views import TodoListCreateView, TodoRetrieveUpdateDestroyView

urlpatterns = [
    path('todoList/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todoList/<int:pk>/', TodoRetrieveUpdateDestroyView.as_view(), name='todo-retrieve-update-destroy'),
]
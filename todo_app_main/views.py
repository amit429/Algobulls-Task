from rest_framework import generics
from .models import ToDoItem , Tag
from .serializers import TodoSerializer, TagSerializer

class TodoListCreateView(generics.ListCreateAPIView):
    """
    API view for creating and listing todo items.
    """
    queryset = ToDoItem.objects.all()
    serializer_class = TodoSerializer

class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific todo item.
    """
    queryset = ToDoItem.objects.all()
    serializer_class = TodoSerializer

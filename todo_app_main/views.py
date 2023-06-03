from rest_framework import generics
from .models import ToDoItem , Tag
from .serializers import TodoSerializer, TagSerializer

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = TodoSerializer

class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = TodoSerializer

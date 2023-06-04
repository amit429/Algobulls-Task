from rest_framework import serializers
from .models import ToDoItem, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = ToDoItem
        fields = '__all__'
    
    def create(self, validated_data):
        """
        Create a new ToDoItem instance with associated tags.
        
        Args:
            validated_data (dict): Validated data for the ToDoItem creation.
        
        Returns:
            todo (ToDoItem): Created ToDoItem instance.
        """
        tags_data = validated_data.pop('tags')
        todo = ToDoItem.objects.create(**validated_data)
        
        existing_tags = {}
        for tag_data in tags_data:
            tag_name = tag_data['name']
            if tag_name in existing_tags:
                tag = existing_tags[tag_name]
            else:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                existing_tags[tag_name] = tag
            todo.tags.add(tag)
            
        return todo
    
    def update(self, instance, validated_data):
        """
        Update an existing ToDoItem instance with associated tags.
        
        Args:
            instance (ToDoItem): Existing ToDoItem instance.
            validated_data (dict): Validated data for the ToDoItem update.
        
        Returns:
            todo (ToDoItem): Updated ToDoItem instance.
        """
        tags_data = validated_data.pop('tags')
        todo = ToDoItem.objects.get(id=instance.id)
        todo.title = validated_data.get('title', todo.title)
        todo.description = validated_data.get('description', todo.description)
        todo.due_date = validated_data.get('due_date', todo.due_date)
        todo.status = validated_data.get('status', todo.status)
        todo.save()
        
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_data['name'])
            todo.tags.add(tag)
        
        return todo

from rest_framework import serializers
from .models import ToDoItem , Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = ToDoItem
        fields = '__all__'

    # def create(self, validated_data):
    #     tags_data = validated_data.pop('tags')
    #     todo = ToDoItem.objects.create(**validated_data)
    #     #check if tag exists, if not create it and if it does, get it
    #     for tag_data in tags_data:
    #         #if the tag exists , without creating duplicate tags add the existing tag to the todo without any tag already exists error
    #         tag, created = Tag.objects.get_or_create(name=tag_data['name'])
    #         todo.tags.add(tag)
    #     return todo
    
    def create(self, validated_data):
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
        tags_data = validated_data.pop('tags')
        todo = ToDoItem.objects.get(id=instance.id)
        todo.title = validated_data.get('title', todo.title)
        todo.description = validated_data.get('description', todo.description)
        todo.due_date = validated_data.get('due_date', todo.due_date)
        todo.status = validated_data.get('status', todo.status)
        todo.save()
        #check if tag exists, if not create it and if it does, get it
        for tag_data in tags_data:
            #if the tag exists , without creating duplicate tags add the existing tag to the todo without any tag already exists error
            tag, created = Tag.objects.get_or_create(name=tag_data['name'])
            todo.tags.add(tag)
        return todo
from django.contrib import admin
from todo_app_main.models import ToDoItem , Tag

admin.site.register(ToDoItem)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date')
    list_filter = ('status', 'due_date')
    fieldsets = (
        ('Task Information', {
            'fields': ('title', 'description', 'due_date', 'tags', 'status')
        }),
    )
    readonly_fields = ('timestamp',)

admin.site.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

# Register your models here.

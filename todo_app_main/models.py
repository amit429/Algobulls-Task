from django.db import models
from django.urls import reverse
from django.utils import timezone

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class ToDoItem(models.Model):

    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    )
    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)   
    due_date = models.DateTimeField(default=one_week_hence)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]
# Create your models here.

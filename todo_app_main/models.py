from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db import DEFAULT_DB_ALIAS

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        #check if tag exists in the database
        existing_tag = Tag.objects.using(DEFAULT_DB_ALIAS).filter(name__iexact=self.name).first()
        if existing_tag:
            self.id = existing_tag.id
        else:
            self.name = self.name.lower()
            super().save(*args, **kwargs)
    
class ToDoItem(models.Model):

    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    )
    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()   
    due_date = models.DateTimeField(default=one_week_hence)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')
    tags = models.ManyToManyField(Tag , null=True, blank=True)

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]
# Create your models here.

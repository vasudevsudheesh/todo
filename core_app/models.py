from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    priority = models.IntegerField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

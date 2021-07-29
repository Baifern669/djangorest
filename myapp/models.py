from django.db import models


# Create your models here. By Fern
class Task(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField()

    def __str__(self):
        return self.title

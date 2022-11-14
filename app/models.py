from django.db import models


class TagModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TaskModel(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(TagModel, related_name="tasks")

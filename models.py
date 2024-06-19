Python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=True)
    assignee = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=50, choices=[('TO_DO', 'To Do'), ('IN_PROGRESS', 'In Progress'), ('DONE', 'Done')])
    deadline = models.DateTimeField(null=True)

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
Usa el código con precaución.
content_copy
Views.py:
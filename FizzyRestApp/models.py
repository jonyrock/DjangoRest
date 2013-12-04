from django.db import models

TASK_STATUSES = ['done', 'downloading', 'waiting', 'error']

class Task(models.Model):
    fileUrl = models.CharField(max_length=400, blank=False)
    title = models.CharField(max_length=400, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=50)
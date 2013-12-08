from django.test.utils import override_settings
from django.db import models
import FizzyRest.settings
import os

TASK_STATUSES = ['done', 'downloading', 'waiting', 'error']

class Task(models.Model):
    fileUrl = models.CharField(max_length=400, blank=False)
    title = models.CharField(max_length=400, blank=False)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    finished = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=50)
    downloadedFileName = models.CharField(max_length=100)
    fileSizeBytes = models.IntegerField(default=0)
    downloadedBytes = models.IntegerField(default=0)
    errorReason = models.CharField(max_length=600, blank=True, default='')
    
    def download_percentage(self):
        if self.fileSizeBytes == 0:
            return 0
        return self.downloadedBytes * 100. / self.fileSizeBytes
    
    def download_percentage_formatted(self):
        return str(int(self.download_percentage()))
    
    def download_url(self):
        return '/static/download/' + self.downloadedFileName
    
    def file_path(self):
        return os.path.join(FizzyRest.settings.DOWNLOAD_DIR, self.downloadedFileName)
    
    @staticmethod
    def task_list():
        return Task.objects.order_by('pk').reverse()
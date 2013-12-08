from django.db import models

TASK_STATUSES = ['done', 'downloading', 'waiting', 'error']

class Task(models.Model):
    fileUrl = models.CharField(max_length=400, blank=False)
    title = models.CharField(max_length=400, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=50)
    downloadedFileName = models.CharField(max_length=100)
    fileSizeBytes = models.IntegerField(default=0)
    downloadedBytes = models.IntegerField(default=0)
    
    def download_percentage(self):
        if self.fileSizeBytes == 0:
            return 0
        return self.downloadedBytes * 100. / self.fileSizeBytes
    
    def download_percentage_formatted(self):
        return str(int(self.download_percentage()))
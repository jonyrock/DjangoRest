from FizzyRestApp.download_manager import STATUS_LOCK_ID
from FizzyRestApp.download_manager.download_worker import DownloadWorker
from FizzyRestApp.models import Task
from django_pglocks import advisory_lock
import os


class DownloadManager:
    @staticmethod
    def add_task(task):
        with advisory_lock(STATUS_LOCK_ID):
            task.status = 'waiting'
            count = Task.objects.filter(status='downloading').count()
            if count >= 3:
                task.save()
                return
            task.status = 'downloading'
            task.save()
        worker = DownloadWorker(task.pk)
        worker.start()

    @staticmethod
    def delete_task(task):
        if task.status != 'downloading' and task.status != 'error':
            if os.path.exists(task.file_path()):
                os.remove(task.file_path())
        task.delete()






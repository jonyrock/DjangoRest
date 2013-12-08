from FizzyRestApp.download_manager.download_worker import DownloadWorker
from FizzyRestApp.models import Task

class DownloadManager:
    @staticmethod
    def add_task(task):
        task.status = 'waiting'
        task.save()
        worker = DownloadWorker(task.pk)
        worker.start()






import os
from threading import Thread
from django_pglocks import advisory_lock
from FizzyRest.settings import DOWNLOAD_DIR
from FizzyRestApp.download_manager import STATUS_LOCK_ID

from FizzyRestApp.models import Task
from random import randint
import urllib2


class DownloadWorker(Thread):
    def __init__(self, pk_):
        Thread.__init__(self)
        self.pk = pk_
    
    def run(self):
        while True:
            if self.pk == None:
                return
            self.download()
            self.pk = None
            with advisory_lock(STATUS_LOCK_ID):
                try:
                    task = Task.objects.filter(status='waiting')[0]
                except:
                    return
                task.status = 'downloading'
                task.save()
                self.pk = task.pk
                    
                    
    def download(self):
        task = Task.objects.get(pk=self.pk)
        try:
            url = task.fileUrl
            file_name = str(randint(1000, 9999)) + '_' +url.split('/')[-1]
    
            u = urllib2.urlopen(url)
    
            meta = u.info()
            file_size = int(meta.getheaders("Content-Length")[0])
            
            
            task.downloadedFileName = file_name
            
            file_name = os.path.join(DOWNLOAD_DIR, file_name)
            f = open(file_name, 'wb')
    
            task.fileSizeBytes = file_size
            task.save()
            file_size_dl = 0
            block_sz = 8192 * 4
            while True:
                buffer = u.read(block_sz)
                if not buffer:
                    break
    
                file_size_dl += len(buffer)
                f.write(buffer)
                keepAlive = self.update_progress_or_get_deleted_flag(file_size_dl)
                if not keepAlive:
                    f.close()
                    os.remove(file_name)
    
            f.close()
    
            task.status = 'done'
            task.downloadedBytes = file_size_dl
            task.save()
        except:
            task.status = 'error'
            task.save()


    def update_progress_or_get_deleted_flag(self, downloaded):
        try:
            task = Task.objects.get(pk=self.pk)
        except Task.DoesNotExist:
            return False
        task.downloadedBytes = downloaded
        task.save(force_update=True)
        return True




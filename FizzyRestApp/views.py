from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from FizzyRestApp.download_manager.download_manager import DownloadManager
from models import Task
from content_type_providers.content_type_provider import create_by_request
import os

@csrf_exempt
def index(request):
    provider = create_by_request(request)
    if request.method == 'GET':
        data = Task.objects.all().order_by('pk').reverse()[:30]
        return provider.index_get(request, data)
    elif request.method == 'POST':
            content_obj = provider.index_post(request)
            if content_obj.is_valid():
                obj = content_obj.get_obj()
                DownloadManager.add_task(obj)
                return redirect('/')
                # return redirect('/tasks/' + str(obj.pk))
            else:
                return provider.response_list_errors(request, 
                                                     { 'errorsList' : content_obj.errors })

def tasks_list(request):
    provider = create_by_request(request)
    if request.method == 'GET':
        manufacturers = Task.objects.all()
        return provider.manufacturers_list_get(request, manufacturers)

def delete_task(task):
    if task.status != 'downloading':
        if os.path.exists(task.file_path()):
            os.remove(task.file_path())
    task.delete()
 
@csrf_exempt
def task_details(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)
    
    provider = create_by_request(request)
    if request.method == 'GET':
        return provider.task_detail_get(request, { 'task': task } )
        
    elif request.method == 'PUT':
        obj = provider.manufacturer_detail_put(request)
        if obj.is_valid():
            obj.save()
            return provider.response_ok()
        else:
            return provider.response_error_list(obj.errors)

    elif request.method == 'DELETE':
        delete_task (task)
        return HttpResponse(status=204)
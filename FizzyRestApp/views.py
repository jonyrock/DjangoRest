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
        tasks = Task.task_list().filter(status='downloading')
        return provider.index_get({'tasks': tasks})
    elif request.method == 'POST':
        content_obj = provider.index_post()
        if content_obj.is_valid():
            obj = content_obj.get_obj()
            DownloadManager.add_task(obj)
            # return redirect('/')
            # return redirect('/tasks/' + str(obj.pk))
            return provider.index_post_ok({'task': obj})
        else:
            return provider.index_post_error({'errorsList': content_obj.errors})


def waiting_list(request):
    provider = create_by_request(request)
    if request.method == 'GET':
        tasks = Task.task_list().filter(status='waiting')
        return provider.waiting_list_get({'tasks': tasks})


def done_list(request):
    provider = create_by_request(request)
    if request.method == 'GET':
        tasks = Task.task_list().filter(status='done')
        return provider.done_list_get({'tasks': tasks})


def error_list(request):
    provider = create_by_request(request)
    if request.method == 'GET':
        tasks = Task.task_list().filter(status='error')
        return provider.error_list_get({'tasks': tasks})


@csrf_exempt
def task_details(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

    provider = create_by_request(request)
    if request.method == 'GET':
        return provider.task_detail_get({'task': task})

    elif request.method == 'PUT':
        obj = provider.task_detail_put()
        if obj.is_valid():
            obj.save()
            return provider.response_ok()
        else:
            return provider.response_error_list(obj.errors)

    elif request.method == 'DELETE':
        DownloadManager.delete_task(task)
        return HttpResponse(status=204)
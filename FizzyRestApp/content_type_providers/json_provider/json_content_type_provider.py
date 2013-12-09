from rest_framework.parsers import JSONParser
from FizzyRestApp.content_type_providers.content_type_provider import ContentTypeProvider
from django.shortcuts import render_to_response
from FizzyRestApp.content_type_providers.json_provider.json_response import JSONResponse
from FizzyRestApp.models import Task
from serializers import TaskSerializer


class JsonContentTypeProvider(ContentTypeProvider):
    def __init__(self, request_):
        self.request = request_

    def index_get(self, data):
        serializer = TaskSerializer(data['tasks'], many=True)
        return JSONResponse(serializer.data)

    def index_post(self):
        data = JSONParser().parse(self.request)
        serializer = TaskSerializer(data=data)
        return serializer

    def waiting_list_get(self, data):
        serializer = TaskSerializer(data['tasks'], many=True)
        return JSONResponse(serializer.data)

    def error_list_get(self, data):
        serializer = TaskSerializer(data['tasks'], many=True)
        return JSONResponse(serializer.data)

    def done_list_get(self, data):
        serializer = TaskSerializer(data['tasks'], many=True)
        return JSONResponse(serializer.data)

    def index_post_ok(self, data):
        return JSONResponse({'status': 'ok'})

    def index_post_error(self, errorsList):
        return JSONResponse(errorsList)
    
    def task_details_put_ok(self):
        return JSONResponse({'status': 'ok'})
    
    def task_details_put_error(self, errorsList):
        return JSONResponse(errorsList)
    
    def task_detail_put(self):
        data = JSONParser().parse(self.request)
        serializer = TaskSerializer(data=data)
        return serializer
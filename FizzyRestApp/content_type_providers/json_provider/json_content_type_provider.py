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
        form = TaskForm(self.request.POST)
        return form
    
    def waiting_list_get(self, data):
        serializer = TaskSerializer(data['tasks'], many=True)
        return JSONResponse(serializer.data)

    def error_list_get(self, data):
        serializer = TaskSerializer(data['tasks'], many=True)
        return JSONResponse(serializer.data)

    def done_list_get(self, data):
        serializer = TaskSerializer(data['tasks'], many=True)
        return JSONResponse(serializer.data)

        
from FizzyRestApp.content_type_providers.content_type_provider import ContentTypeProvider
from django.shortcuts import render_to_response
from FizzyRestApp.models import Task
from serializers import TaskSerializer


class JsonContentTypeProvider(ContentTypeProvider):
    
    def __init__(self, request_):
        self.request = request_
    
        
    
        
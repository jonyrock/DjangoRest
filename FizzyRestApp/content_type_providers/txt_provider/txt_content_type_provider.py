from FizzyRestApp.content_type_providers.content_type_provider import ContentTypeProvider
from django.shortcuts import render_to_response, redirect

class TxtContentTypeProvider(ContentTypeProvider):
    def __init__(self, request_):
        self.request = request_

    def index_get(self, data):
        return render_to_response("txt/index.txt", data)

    def waiting_list_get(self, data):
        return render_to_response("txt/waiting_list.txt", data)

    def error_list_get(self, data):
        return render_to_response("txt/error_list.txt", data)

    def done_list_get(self, data):
        return render_to_response("txt/done_list.txt", data)

    def task_detail_get(self, data):
        return render_to_response("txt/task_detail.txt", data)
    
    
        
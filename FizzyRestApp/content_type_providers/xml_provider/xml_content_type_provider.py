from FizzyRestApp.content_type_providers.content_type_provider import ContentTypeProvider
from django.shortcuts import render_to_response, redirect

class XmlContentTypeProvider(ContentTypeProvider):
    def __init__(self, request_):
        self.request = request_

    def index_get(self, data):
        return render_to_response("xml/index.xml", data)

    def waiting_list_get(self, data):
        return render_to_response("xml/waiting_list.xml", data)

    def error_list_get(self, data):
        return render_to_response("xml/error_list.xml", data)

    def done_list_get(self, data):
        return render_to_response("xml/done_list.xml", data)

    def task_detail_get(self, data):
        return render_to_response("xml/task_detail.xml", data)
    
    
        
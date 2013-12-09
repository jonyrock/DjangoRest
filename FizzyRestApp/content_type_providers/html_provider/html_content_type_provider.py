from FizzyRestApp.content_type_providers.content_type_provider import ContentTypeProvider
from django.shortcuts import render_to_response, redirect
from FizzyRestApp.models import Task
from forms import TaskForm


class HtmlContentTypeProvider(ContentTypeProvider):
    def __init__(self, request_):
        self.request = request_

    def index_get(self, data):
        data.update({'form': TaskForm()})
        return render_to_response("html/index.html", data)

    def index_post(self):
        form = TaskForm(self.request.POST)
        return form

    def waiting_list_get(self, data):
        return render_to_response("html/waiting_list.html", data)

    def error_list_get(self, data):
        return render_to_response("html/error_list.html", data)

    def done_list_get(self, data):
        return render_to_response("html/done_list.html", data)

    def task_detail_get(self, data):
        return render_to_response("html/task_detail.html", data)

    def index_post_ok(self, data):
        return redirect('/tasks/' + str(data['task'].pk))

    def index_post_error(self, errorsList):
        return render_to_response("html/errors_list.html", errorsList)
    
    
        
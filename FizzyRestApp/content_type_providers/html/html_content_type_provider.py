from FizzyRestApp.content_type_providers.content_type_provider import ContentTypeProvider
from django.shortcuts import render_to_response
from FizzyRestApp.models import Task
from forms import TaskForm


class HtmlContentTypeProvider(ContentTypeProvider):
    def index_get(self, request, data):
        return render_to_response("html/index.html",
                                  {'data': data,
                                   'form': TaskForm()
                                  })

    def index_post(self, request):
        form = TaskForm(request.POST)
        return form

    def tasks_list_get(self, request, data):
        return render_to_response("html/task_list.html", data)

    def task_detail_get(self, request, data):
        return render_to_response("html/task_detail.html", data)

    def response_ok(self, request):
        return render_to_response("html/ok.html")

    def response_list_errors(self, request, errorsList):
        return render_to_response("html/errors_list.html", errorsList)
    
    
        
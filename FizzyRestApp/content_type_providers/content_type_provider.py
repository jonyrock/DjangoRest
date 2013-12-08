def create_by_request(request):
    from html_provider.html_content_type_provider import HtmlContentTypeProvider
    from json_provider.json_content_type_provider import JsonContentTypeProvider
    if request.META['HTTP_ACCEPT'] == 'application/json':
        return JsonContentTypeProvider(request)
    return HtmlContentTypeProvider(request)


class ContentTypeProvider:
    def index_get(self, data):
        pass

    def index_post(self):
        pass

    def waiting_list_get(self, data):
        pass

    def error_list_get(self, data):
        pass

    def done_list_get(self, data):
        pass

    def task_detail_get(self, data):
        pass

    def task_detail_put(self, data):
        pass

    def response_ok(self):
        pass

    def response_list_errors(self, errorsList):
        pass

 
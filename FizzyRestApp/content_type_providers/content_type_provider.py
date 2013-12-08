def create_by_request(request):
    from html.html_content_type_provider import HtmlContentTypeProvider

    return HtmlContentTypeProvider()


class ContentTypeProvider:
    def index_get(self, request, data):
        pass

    def index_post(self, request, data):
        pass

    def waiting_list_get(self, request, data):
        pass

    def done_list_get(self, request, data):
        pass

    def task_detail_get(self, request, data):
        pass

    def task_detail_put(self, request, data):
        pass

    def response_ok(self, request):
        pass

    def response_list_errors(self, request, errorsList):
        pass

 
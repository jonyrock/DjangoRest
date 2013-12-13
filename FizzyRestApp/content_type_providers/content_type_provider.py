from django.http import HttpResponse


def create_by_request(request):
    from html_provider.html_content_type_provider import HtmlContentTypeProvider
    from json_provider.json_content_type_provider import JsonContentTypeProvider
    from txt_provider.txt_content_type_provider import TxtContentTypeProvider
    from xml_provider.xml_content_type_provider import XmlContentTypeProvider
    if request.META['HTTP_ACCEPT'].startswith('application/json'):
        return JsonContentTypeProvider(request)
    if request.META['HTTP_ACCEPT'].startswith('text/html'):
        return HtmlContentTypeProvider(request)
    if request.META['HTTP_ACCEPT'].startswith('text/plain'):
        return TxtContentTypeProvider(request)
    if request.META['HTTP_ACCEPT'].startswith('application/xml'):
        return XmlContentTypeProvider(request)
    
    return HttpResponse(status=206)


class ContentTypeProvider:
    def index_get(self, data):
        pass

    def index_post(self):
        pass
    
    def index_post_ok(self, data):
        pass
    
    def index_post_error(self, errorsList):
        pass

    def waiting_list_get(self, data):
        pass

    def error_list_get(self, data):
        pass

    def done_list_get(self, data):
        pass

    def task_detail_get(self, data):
        pass

    def task_detail_put(self):
        pass
    
    def task_details_put_ok(self):
        pass
    
    def task_details_put_error(self, errorsList):
        pass

    


 
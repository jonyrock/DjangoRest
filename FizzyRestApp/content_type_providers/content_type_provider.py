

def create_by_request(request):
    from html.html_content_type_provider import HtmlContentTypeProvider 
    return HtmlContentTypeProvider()

class ContentTypeProvider:
    
    def index_get(self, request, data):
        pass
    
    def index_post(self, request, data):
        """
        Return parsed from http object like 
        Form or Serializer with is_valid() method
        """
        pass

    def manufacturers_list_get(self, request, data):
        pass

    def manufacturer_detail_get(self, request, data):
        pass

    def manufacturer_detail_put(self, request, data):
        """
        Return parsed from http object to save
        """
        pass

    def response_ok(self, request):
        pass

    def response_list_errors(self, request, errorsList):
        pass

 
class ContentTypeProvider:
    def create_by_request(request):
        return

    def index_get(self, request, data):
        pass

    def manufacturers_list_get(self, request, data):
        pass

    def manufacturers_list_post(self, request, data):
        """
        Return parsed from http object to save
        """
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

    
 
from FizzyRestApp.content_type_providers.content_type_provider import ContentTypeProvider
from django.shortcuts import render_to_response
from FizzyRestApp.models import Manufacturer

class HtmlContentTypeProvider(ContentTypeProvider):
    def index_get(self, request, data):
        return render_to_response("html/index.html", data)
    
    def index_post(self, request):
        m = Manufacturer()
        m.title = m.POST['manufacturer-title']
        m.yearFounded = m.POST['manufacturer-yearFounded']
        m.imageUrl = m.POST['manufacturer-imageUrl']
        return m

    def manufacturers_list_get(self, request, data):
        return render_to_response("html/manufacturers_list.html", data)
    
    
        
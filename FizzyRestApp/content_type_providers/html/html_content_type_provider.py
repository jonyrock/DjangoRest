from FizzyRestApp.content_type_providers.content_type_provider import ContentTypeProvider
from django.shortcuts import render_to_response


class HtmlContentTypeProvider(ContentTypeProvider):
    def index_get(self, request, data):
        return render_to_response("index.html", data)

    def manufacturers_list_get(self, request, data):
        return render_to_response("manufacturers_list.html", data)
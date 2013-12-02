
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import Manufacturer, Drink
from content_type_providers.content_type_provider import create_by_request

@csrf_exempt
def index(request):
    provider = create_by_request(request)
    if request.method == 'GET':
        data = Manufacturer.objects.all()
        return provider.index_get(request, data)
    elif request.method == 'POST':
            obj = provider.index_post(request)
            if obj.is_valid():
                obj.save()
                return provider.response_ok(request)
            else:
                return provider.response_list_errors(obj.errors)

def manufacturers_list(request):
    provider = create_by_request(request)
    if request.method == 'GET':
        manufacturers = Manufacturer.objects.all()
        return provider.manufacturers_list_get(request, manufacturers)
    

@csrf_exempt
def manufacturer_detail(request, pk):
    """
    Retrieve, update or delete a manufacturer info.
    """
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
    except Manufacturer.DoesNotExist:
        return HttpResponse(status=404)
    
    provider = create_by_request(request)
    if request.method == 'GET':
        return provider.manufacturer_detail_get(request, { manufacturer: manufacturer } )
        
    elif request.method == 'PUT':
        obj = provider.manufacturer_detail_put(request)
        if obj.is_valid():
            obj.save()
            return provider.response_ok()
        else:
            return provider.response_error_list(obj.errors)

    elif request.method == 'DELETE':
        manufacturer.delete()
        return HttpResponse(status=204)
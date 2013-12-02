
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import Manufacturer, Drink
from serializers import ManufacturerSerializer

def index(request):
    return manufacturers_list(request)

@csrf_exempt
def manufacturers_list(request):
    if request.method == 'GET':
        manufacturers = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(manufacturers, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def manufacturer_detail(request, pk):
    """
    Retrieve, update or delete a manufacturer info.
    """
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
    except Manufacturer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(manufacturer)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(manufacturer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        manufacturer.delete()
        return HttpResponse(status=204)
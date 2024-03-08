# from django.http import JsonResponse
from  rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GroceryListSerializer
from .models import GroceryList

@api_view (['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/groceryList/',
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns an array of products'
        },
        {
            'Endpoint': '/groceryList/id',
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns a single product'
        },
        {
            'Endpoint': '/groceryList/create',
            'method' : 'POST',
            'body' : {'body': ""},
            'description' : 'Create list'
        },
        {
            'Endpoint': '/groceryList/id/update',
            'method' : 'PUT',
            'body' : {'body':""},
            'description' : 'updates the list'
        },
        {
            'Endpoint': '/groceryList/id/delete',
            'method' : 'DELETE',
            'body' : None,
            'description' : 'Deletes existing product'
        }
    ]
    return Response(routes)

@api_view(['GET'])
def getGroceryList(request):
    grocerylists = GroceryList.objects.all()
    serializer = GroceryListSerializer(grocerylists, many=True)
    return Response(serializer.data)
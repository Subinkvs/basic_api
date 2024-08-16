from .serializers import DrinkSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Drinks
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def drink_list(request):
    drinks = Drinks.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return Response({'drinks':serializer.data})

@api_view(['POST'])
def drink_list_create(request):
    serializer = DrinkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def drinks_detail_view(request, id):
    drink = Drinks.objects.get(pk=id)
    if request.method == 'GET':
        try:
            drink = Drinks.objects.get(pk=id)
        except Drinks.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DrinkSerializer(drink)
        return Response({'drinks':serializer.data})
    
    if request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


 
    

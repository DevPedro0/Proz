from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Product, SerializersProductAPI, User, SerializerCreateUser
from django.shortcuts import get_object_or_404

# Definindo routers

@api_view(http_method_names=["POST", "GET"])
def ProductRecipeView(request):
    if (request.method == "GET"):
        product = Product.objects.all()
        serializer = SerializersProductAPI(product, many = True)
        return Response(serializer.data)
    
    elif (request.method == "POST"):
        serializer = SerializersProductAPI(data = request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view()
def ProductRecipeViewFilter(request, pk):
    product = get_object_or_404(
        Product.objects.filter(pk = pk)
    )
    serializer = SerializersProductAPI(product)
    return Response(
        serializer.data,
    )

# ApiView para Criar Usuários com Dados Via API
@api_view(http_method_names=["POST", "GET"])
def APICreateUser(request):
    
    if (request.method == "POST"):
        serializer = SerializerCreateUser(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    elif (request.method == "GET"):
        user = User.objects.all()
        serializer = SerializerCreateUser(user, many =True)
        return Response(serializer.data)
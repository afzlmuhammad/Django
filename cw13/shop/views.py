from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import ProductForm
from .models import Product

@api_view(['POST'])
def create_product(request):
    form = ProductForm(request.data)

    if form.is_valid():
        product = form.save()
        return Response(
            {'id': product.id},
            status=status.HTTP_201_CREATED
        )

    return Response(
        form.errors,
        status=status.HTTP_400_BAD_REQUEST
    )
    
    

from .serializers import ProductSerializer

@api_view(['GET'])
def list_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


from django.shortcuts import get_object_or_404

@api_view(['PUT'])
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    form = ProductForm(request.data, instance=product)

    if form.is_valid():
        form.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    return Response(
        form.errors,
        status=status.HTTP_400_BAD_REQUEST
    )
    
    
    
@api_view(['DELETE'])
def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(
            {'error': 'Product not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    product.delete()

    return Response(
        {'message': 'Product deleted successfully'},
        status=status.HTTP_200_OK
    )
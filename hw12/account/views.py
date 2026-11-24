from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def list_products(request):

    products = [
        {
            'name': 'Laptop',
            'price': 55000,
            'category': 'Electronics'
        },
        {
            'name': 'Mobile',
            'price': 20000,
            'category': 'Electronics'
        },
        {
            'name': 'Shoes',
            'price': 1500,
            'category': 'Fashion'
        }
    ]

    return Response(products)
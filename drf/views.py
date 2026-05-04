from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.exceptions import NotFound

# @api_view(["GET"])
# def get_products(req):
#     products = Product.objects.all()  
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)

@api_view(["GET"])
def get_product(req, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        raise NotFound("Product not found")
    
    serializer = ProductSerializer(product)
    return Response(serializer.data)

# @api_view(["POST"])
# def create_products(req):
#     serializer = ProductSerializer(data=req.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)

# @api_view(["PUT", "PATCH"])
# def update_product(req, pk):
#     product = get_object_or_404(Product, id=pk)
#     serializer = ProductSerializer(product, data=req.data, partial=True)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)

# @api_view(["DELETE"])
# def delete_product(req, pk):
#     product = f=get_object_or_404(Product, id=pk)
#     product.delete()
#     return Response({"msg:Product Delete Successful!"})

# class ProductAPI(APIView):

#     authentication_classes=[TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, req):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
    
#     def post(self, req):
#         serializer = ProductSerializer(data=req.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# class ProductViewSet(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class FilterProduct(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        price = self.request.query_params.get('price')
        return Product.objects.filter(price=price)

class ProductListCreate(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

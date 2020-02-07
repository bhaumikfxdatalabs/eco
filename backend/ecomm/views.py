from django.shortcuts import render
from rest_framework import generics
from ecomm.models import Product
from ecomm.serializers import ProductSerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = [MultiPartParser, FormParser]


class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def get_object(self):
    #     product = Product.objects.filter(id=pk)
    #     return product

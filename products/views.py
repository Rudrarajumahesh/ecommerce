from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from . models import Product
from .serializers import ProductSerializer

# Create your views here.


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
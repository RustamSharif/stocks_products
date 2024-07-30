# from rest_framework.viewsets import ModelViewSet
#
# from logistic.models import Product, Stock
# from logistic.serializers import ProductSerializer, StockSerializer
#
#
# class ProductViewSet(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # при необходимости добавьте параметры фильтрации
#
#
# class StockViewSet(ModelViewSet):
#     queryset = Stock.objects.all()
#     serializer_class = StockSerializer
#     # при необходимости добавьте параметры фильтрации
# File: logistic/views.py

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [SearchFilter]
    search_fields = ['positions__product__title', 'positions__product__description']
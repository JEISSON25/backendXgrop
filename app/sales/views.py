from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django_filters import rest_framework as django_filters


class SalesViewset(viewsets.ModelViewSet):

    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = ([JWTAuthentication])

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')


class FilterSales(django_filters.FilterSet):
    date_range = django_filters.DateFromToRangeFilter(field_name='date')
    products = django_filters.NumberFilter(field_name='products')

    class Meta:
        model = Sales
        fields = ['date_range', 'products']


class SalesProductViewset(viewsets.ModelViewSet):

    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    filter_backends = [django_filters.DjangoFilterBackend]
    filterset_class = FilterSales
    # permission_classes = [IsAuthenticated]
    # authentication_classes = ([JWTAuthentication])

    def get_queryset(self):
        queryset = Sales.objects.all()

        start_date = self.request.query_params.get('date_range_after', None)
        end_date = self.request.query_params.get('date_range_before', None)
        products = self.request.query_params.get('products', None)

        if start_date and end_date and products:
            queryset = queryset.filter(date__range=[start_date, end_date])

        return queryset

from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework import filters, status
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response


class AccountCreateView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer
    # Permitir la creación de usuarios sin autenticació
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class AccountViewset(viewsets.ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = ([JWTAuthentication])

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')


class TypeAccountViewset(viewsets.ModelViewSet):

    queryset = TypeAccount.objects.all()
    serializer_class = TypeAccountSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = ([JWTAuthentication])

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')

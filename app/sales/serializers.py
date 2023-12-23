from rest_framework import serializers
from .models import *
from ..products.serializers import *
# from ..account.serializers import AccountSerializer


class SalesSerializer(serializers.ModelSerializer):
    products = ProductsSerializer(read_only=True)
    products_id = serializers.IntegerField(required=False)
    # account = AccountSerializer(read_only=True)
    # account_id = serializers.IntegerField(required=False)

    class Meta:
        model = Sales
        fields = ('__all__')

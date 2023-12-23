from rest_framework import serializers
from .models import *


class TypeAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeAccount
        fields = ('__all__')


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('__all__')


class AccountCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ['username', 'password',
                  'first_name', 'last_name', 'type_account']

    def create(self, validated_data):
        user = Account.objects.create_user(**validated_data)
        return user

from django.db.models import fields
from rest_framework import serializers

from .models import Currency, Category, Transaction

class CurrencySerializers(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'code','name')

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')

class TransactionSerializers(serializers.ModelSerializer):
    currency = serializers.SlugRelatedField(slug_field='code', queryset= Currency.objects.all())

    class Meta:
        model = Transaction
        fields = (
            "id",
            "amount",
            "currency",
            "date",
            "description",
            "category"
        )
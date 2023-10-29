from rest_framework import serializers
from Catalog.models import *


class ReadProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'label',
            'description',
            'image',
            'price',
            'category',
            'has_valid_discount',
            'discount',
            'discounted_price')


class ReadSubcategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',
                  'label',
                  'parent',
                  'icon',
                  'subcategories',
                  'products'
                  )


class CategorySerializer(serializers.ModelSerializer):
    subcategories = ReadSubcategoriesSerializer(many=True, read_only=True)
    products = ReadProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id',
                  'label',
                  'parent',
                  'icon',
                  'subcategories',
                  'products'
                  )


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id',
                  'start_date',
                  'end_date',
                  'percentage',
                  'is_valid')


class ProductSerializer(serializers.ModelSerializer):
    discount = DiscountSerializer()
    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='label')

    class Meta:
        model = Product
        fields = (
            'id',
            'label',
            'description',
            'image',
            'price',
            'category',
            'has_valid_discount',
            'discount',
            'discounted_price')



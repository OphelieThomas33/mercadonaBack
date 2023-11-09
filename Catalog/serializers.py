from rest_framework import serializers
from Catalog.models import *


# Information on promotions for discount to send to the API
class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id',
                  'start_date',
                  'end_date',
                  'percentage',
                  'is_valid')


# Information to send to the API
class ReadCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',
                  'label',
                  'parent',
                  'icon',
                  'subcategories',
                  'products'
                  )


# serializer allowing the display of products in categories
class ReadProductSerializer(serializers.ModelSerializer):
    discount = DiscountSerializer()
    category = ReadCategorySerializer(many=True)

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


# serializer allowing the display of subcategories in categories
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


# Information on categories to send to the API
class CategorySerializer(serializers.ModelSerializer):
    # call to a readOnlySerializer to allow the display of subcategories and products
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


# Information on products to send to the API
class ProductSerializer(serializers.ModelSerializer):
    # call to a readOnlySerializer to allow the display of categories and discount
    discount = DiscountSerializer()
    category = CategorySerializer(many=True)

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

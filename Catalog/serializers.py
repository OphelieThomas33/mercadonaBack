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
    category = CategorySerializer(many=True)
    # image = serializers.SerializerMethodField()

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

    # def get_image_url(self, product):
    #     request = self.context.get('request')
    #     image = product.image.url
    #     return request.build_absolute_uri(image)





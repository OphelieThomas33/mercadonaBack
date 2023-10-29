from rest_framework import serializers
from Catalog.models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'label', 'parent', 'subcategories', 'icon',)

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['subcategories'] = CategorySerializer(many=True)
        return fields


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id', 'start_date', 'end_date', 'percentage', 'is_valid')


class ProductSerializer(serializers.ModelSerializer):
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



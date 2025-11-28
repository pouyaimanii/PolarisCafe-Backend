from rest_framework import serializers
from .models import ProductModel, CategoryModel



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ["id", "name", "image", "description", "price", "category" , "available"]


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = CategoryModel
        fields = ["id", "name", "image", "description", "products"]
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CategoryModel, ProductModel
from .serializers import CategorySerializer, ProductSerializer
from django.shortcuts import get_object_or_404



class CategoryListView(APIView):
    def get(self, request):
        try:
            categories = CategoryModel.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error" : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
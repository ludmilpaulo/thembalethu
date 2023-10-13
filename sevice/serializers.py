from rest_framework import serializers
from .models import Category, Service

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'category', 'name', 'slug', 'image', 'description', 'price', 'available', 'created', 'updated']

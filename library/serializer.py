from rest_framework import serializers
from .models import LibraryTopCategory, LibraryMiddleCategory, LibrarySubCategory, LibraryData

class LibraryTopCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryTopCategory
        fields = '__all__'

class LibraryMiddleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryMiddleCategory
        fields = '__all__'

class LibrarySubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibrarySubCategory
        fields = '__all__'

class LibraryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryData
        fields = '__all__'
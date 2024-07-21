from rest_framework import serializers
from .models import Testimony

class TestimonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimony
        fields = ['id', 'user', 'title', 'description', 'status', 'created_at', 'updated_at']

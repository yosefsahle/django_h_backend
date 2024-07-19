# consult/serializers.py
from rest_framework import serializers
from .models import Consultant, ConsultingType, ConsultantAvailability, Booking

class ConsultingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultingType
        fields = '__all__'

class ConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultant
        fields = '__all__'

class ConsultantAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultantAvailability
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

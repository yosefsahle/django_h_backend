from rest_framework import serializers
from .models import OTP
from django.contrib.auth import get_user_model

User = get_user_model()

class OTPRequestSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    request_type = serializers.ChoiceField(choices=[('registration', 'Registration'),('reset','Reset')])

    def validate(self,data):
        phone_number = data['phone_number']
        request_type = data['request_type']

        if request_type == 'registration':
            if User.objects.filter(phone=phone_number).exists():
                raise serializers.ValidationError('User account already exists.')
        elif request_type == 'reset':
            if not User.objects.filter(phone=phone_number).exists():
                raise serializers.ValidationError('User not registered')
        return data

class OTPValidateSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    otp_code = serializers.CharField(max_length=5)
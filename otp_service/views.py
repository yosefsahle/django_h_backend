from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import OTPRequestSerializer, OTPValidateSerializer
from .models import OTP
from django.utils.crypto import get_random_string
from django.utils import timezone

class OTPRequestView(generics.GenericAPIView):
    serializer_class = OTPRequestSerializer
    permission_classes = [AllowAny]

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone_number']
        otp_code = get_random_string(length=5,allowed_chars='0123456789')

        otp_record, created = OTP.objects.update_or_create(
            phone_number=phone_number,
            defaults={'otp_code':otp_code,'attempts':0,'created_at':timezone.now()}
        )

        return Response({'detail':'OTP sent successfully.'},status=status.HTTP_200_OK)
    
class OTPValidateView(generics.GenericAPIView):
    serializer_class = OTPValidateSerializer
    permission_classes = [AllowAny]

    def post(self,request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone_number']
        otp_code = serializer.validated_data['otp_code']

        try:
            otp_record = OTP.objects.get(phone_number=phone_number)
            if otp_record.is_expired():
                otp_record.delete()
                return Response({'detail':'OTP expired.'},status=status.HTTP_400_BAD_REQUEST)
            
            if otp_record.otp_code == otp_code:
                otp_record.delete()
                return Response({'detail':'OTP Validated Successfully.'},status=status.HTTP_200_OK)
            else:
                otp_record.attempts += 1
                otp_record.save()
                if otp_record.attempts >= 3:
                    otp_record.delete()
                    return Response({'detail':'OTP invalid. Attempts exceeded'},status=status.HTTP_400_BAD_REQUEST)
                return Response({'detail':'OTP invalid'},status=status.HTTP_400_BAD_REQUEST)
        except OTP.DoesNotExist:
            return Response({'detail':'OTP not found. Resend OTP'},status=status.HTTP_400_BAD_REQUEST)
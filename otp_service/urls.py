from django.urls import path
from .views import OTPRequestView, OTPValidateView

urlpatterns = [
    path('request/', OTPRequestView.as_view(), name='otp-request'),
    path('validate/', OTPValidateView.as_view(), name='otp-validate'),
]
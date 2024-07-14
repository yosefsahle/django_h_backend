from django.db import models
from django.utils import timezone
from datetime import timedelta

class OTP(models.Model):
    phone_number = models.CharField(max_length=15)
    otp_code = models.CharField(max_length=5)
    attempts = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=10)
    
    def __str__(self):
        return f"{self.phone_number} - {self.otp_code}"

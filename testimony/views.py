from rest_framework import generics, permissions
from .models import Testimony
from .serializer import TestimonySerializer
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser

class TestimonyCreateAPIView(generics.CreateAPIView):
    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer
    permission_classes = [IsAuthenticated]

class TestimonyUpdateAPIView(generics.UpdateAPIView):
    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer
    permission_classes = [IsAdminUser]

class TestimonyDeleteAPIView(generics.DestroyAPIView):
    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer
    permission_classes = [IsAdminUser]

class ActiveTestimonyListAPIView(generics.ListAPIView):
    serializer_class = TestimonySerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        return Testimony.objects.filter(status='At')

class DeactiveTestimonyListAPIView(generics.ListAPIView):
    serializer_class = TestimonySerializer
    permission_classes = [IsAdminUser]
    def get_queryset(self):
        return Testimony.objects.filter(status='Dt')

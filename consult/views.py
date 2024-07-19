# consult/views.py
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ConsultingType, Consultant, ConsultantAvailability, Booking
from .serializer import (
    ConsultingTypeSerializer, ConsultantSerializer,
    ConsultantAvailabilitySerializer, BookingSerializer
)
from rest_framework.permissions import AllowAny

class ConsultingTypeListCreateView(ListCreateAPIView):
    queryset = ConsultingType.objects.all()
    serializer_class = ConsultingTypeSerializer
    permission_classes = [AllowAny]

class ConsultingTypeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ConsultingType.objects.all()
    serializer_class = ConsultingTypeSerializer
    permission_classes = [AllowAny]

class ConsultantListCreateView(ListCreateAPIView):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer
    permission_classes = [AllowAny]

class ConsultantDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer
    permission_classes = [AllowAny]

class ConsultantAvailabilityListCreateView(ListCreateAPIView):
    queryset = ConsultantAvailability.objects.all()
    serializer_class = ConsultantAvailabilitySerializer
    permission_classes = [AllowAny]

class ConsultantAvailabilityDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ConsultantAvailability.objects.all()
    serializer_class = ConsultantAvailabilitySerializer
    permission_classes = [AllowAny]

class BookingListCreateView(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]

class BookingDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]

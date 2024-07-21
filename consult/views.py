# consult/views.py
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ConsultingType, Consultant, ConsultantAvailability, Booking,ConsultantType
from .serializer import (
    ConsultingTypeSerializer, ConsultantSerializer,
    ConsultantAvailabilitySerializer, BookingSerializer,
)
from rest_framework.permissions import AllowAny
from rest_framework import  status
from rest_framework.response import Response
from django.utils import timezone


from rest_framework.views import APIView
from datetime import datetime, timedelta
from django.db.models import Q

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



class AvailableConsultantView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        consulting_type_id = request.query_params.get('consulting_type_id')

        if not consulting_type_id:
            return Response({"error": "consulting_type_id parameter is required"}, status=400)

        today = timezone.now().date()
        week_start = today - timedelta(days=today.weekday())  # Monday of the current week

        def get_week_range(week_number):
            start_date = week_start + timedelta(weeks=week_number - 1)
            end_date = start_date + timedelta(days=6)
            return start_date, end_date

        def get_availabilities(week_number):
            start_date, end_date = get_week_range(week_number)
            bookings_in_week = Booking.objects.filter(
                consultan_availability__in=availabilities,
                book_date__range=[start_date, end_date]
            ).values_list('consultan_availability_id', flat=True)

            return [
                availability for availability in availabilities
                if availability.id not in bookings_in_week
            ]

        # Fetch all consultants for the given consulting type
        consultants = Consultant.objects.filter(
            consultanttype__consulting_type_id=consulting_type_id
        )

        # Fetch all availabilities for the consultants
        availabilities = ConsultantAvailability.objects.filter(
            consultant__in=consultants
        )

        weeks_availabilities = {}

        for week_number in range(1, 5):
            week_availabilities = get_availabilities(week_number)
            weeks_availabilities[f'week_{week_number}'] = [
                {
                    'day_of_week': availability.day_of_the_week,
                    'available_time': availability.available_time
                } for availability in week_availabilities
            ]

        return Response(weeks_availabilities)

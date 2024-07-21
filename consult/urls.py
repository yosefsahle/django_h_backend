# consult/urls.py
from django.urls import path
from .views import (
    ConsultingTypeListCreateView, ConsultingTypeDetailView,
    ConsultantListCreateView, ConsultantDetailView,
    ConsultantAvailabilityListCreateView, ConsultantAvailabilityDetailView,
    BookingListCreateView, BookingDetailView,AvailableConsultantView
)

urlpatterns = [
    path('consulting-types/', ConsultingTypeListCreateView.as_view(), name='consulting-type-list-create'),
    path('consulting-types/<int:pk>/', ConsultingTypeDetailView.as_view(), name='consulting-type-detail'),

    path('consultants/', ConsultantListCreateView.as_view(), name='consultant-list-create'),
    path('consultants/<int:pk>/', ConsultantDetailView.as_view(), name='consultant-detail'),

    path('consultant-availability/', ConsultantAvailabilityListCreateView.as_view(), name='consultant-availability-list-create'),
    path('consultant-availability/<int:pk>/', ConsultantAvailabilityDetailView.as_view(), name='consultant-availability-detail'),

    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),

    path('available-consultants/', AvailableConsultantView.as_view(), name='available-consultants'),
]

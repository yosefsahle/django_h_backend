from django.urls import path
from .views import (
    TestimonyCreateAPIView,
    TestimonyUpdateAPIView,
    TestimonyDeleteAPIView,
    ActiveTestimonyListAPIView,
    DeactiveTestimonyListAPIView,
)

urlpatterns = [
    path('create/', TestimonyCreateAPIView.as_view(), name='testimony-create'),
    path('update/<int:pk>/', TestimonyUpdateAPIView.as_view(), name='testimony-update'),
    path('delete/<int:pk>/', TestimonyDeleteAPIView.as_view(), name='testimony-delete'),
    path('active/', ActiveTestimonyListAPIView.as_view(), name='active-testimonies'),
    path('deactive/', DeactiveTestimonyListAPIView.as_view(), name='deactive-testimonies'),
]

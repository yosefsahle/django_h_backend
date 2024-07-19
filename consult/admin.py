# consult/admin.py
from django.contrib import admin
from .models import ConsultingType, Consultant, ConsultantType, ConsultantAvailability, Booking

admin.site.register(ConsultingType)
admin.site.register(Consultant)
admin.site.register(ConsultantType)
admin.site.register(ConsultantAvailability)
admin.site.register(Booking)

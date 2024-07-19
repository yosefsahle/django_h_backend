# consult/models.py
from django.db import models
from user.models import User

class ConsultingType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Consultant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    consulting_types = models.OneToOneField(ConsultingType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.fullname

class ConsultantType(models.Model):
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    consulting_type = models.ForeignKey(ConsultingType, on_delete=models.CASCADE)

class ConsultantAvailability(models.Model):
    DAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    day_of_the_week = models.CharField(max_length=3, choices=DAY_CHOICES)
    available_time = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.consultant.user.username} - {self.get_day_of_the_week_display()} - {self.available_time}"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('taken', 'Taken'),
        ('contacted', 'Contacted'),
        ('not-contacted', 'Not Contacted'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE,null=True,blank=True)
    consulting_type = models.ForeignKey(ConsultingType, on_delete=models.CASCADE)
    day = models.DateField()
    time_slot = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.consulting_type.name} - {self.day} - {self.time_slot}"

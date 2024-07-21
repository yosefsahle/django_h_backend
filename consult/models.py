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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.fullname


class ConsultantType(models.Model):
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    consulting_type = models.ForeignKey(ConsultingType, on_delete=models.CASCADE)

class ConsultantAvailability(models.Model):
    DAY_CHOICES = [
        ('Mon', 'Mon'),
        ('Tue', 'Tue'),
        ('Wed', 'Wed'),
        ('Thu', 'Thu'),
        ('Fri', 'Fri'),
        ('Sat', 'Sat'),
        ('Sun', 'Sun'),
    ]
    TIME_CHOICES = [
        ('1:00-3:00 Am','1:00-3:00 Am'),
        ('3:00-5:00 Am','3:00-5:00 Am'),
        ('5:00-7:00 Am','5:00-7:00 Am'),
        ('7:00-9:00 Am','7:00-9:00 Am'),
        ('9:00-11:00 Am','9:00-11:00 Am'),
        ('12:00-1:00 pm','12:00-1:00 pm'),
        ('1:00-3:00 pm','1:00-3:00 pm'),
    ]
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    day_of_the_week = models.CharField(max_length=3, choices=DAY_CHOICES)
    available_time = models.CharField(max_length=100,choices=TIME_CHOICES)

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
    consultan_availability = models.ForeignKey(ConsultantAvailability,on_delete=models.DO_NOTHING)
    book_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.consulting_type.name} - {self.consultan_availability}"

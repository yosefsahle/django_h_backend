from django.db import models
from user.models import User

class Consultant(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    consulting_type = models.TextField()

    def __str__(self):
        return self.user.fullname

class ConsultantAvailability(models.Model):
    DAY_CHOICES = (
        ('Mon','Monday'),
        ('Tus','Tuesday'),
        ('Wed','Wedensday'),
        ('Thu','Thursday'),
        ('Fri','Friday'),
        ('Sat','Saturday'),
        ('Sun','Sunday')
    )
    consultant = models.ForeignKey(Consultant,on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20,choices=DAY_CHOICES)
    available_time = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.consultant.user.fullname} - {self.day_of_week} - {self.available_time}"
    
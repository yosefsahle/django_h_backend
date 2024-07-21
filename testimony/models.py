from django.db import models
from user.models import User

class Testimony(models.Model):
    STATUS_CHOICES = (
        ('At', 'Active'),
        ('Dt', 'Deactive'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Dt')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

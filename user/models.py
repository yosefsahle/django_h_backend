from django.db import models
from django.contrib.auth.models import AbstractUser
import os

class User(AbstractUser):
    ROLE_TYPES = (
        ('U', 'User'),
        ('FPM', 'Feeds Post Manager'),
        ('NPM', 'News Post Manager'),
        ('PM', 'Post Manager'),
        ('C', 'Consultant'),
        ('A', 'Admin'),
        ('SA', 'Super Admin'),
    )
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True)
    fullname = models.CharField(max_length=255, unique=False)
    church = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=30, choices=ROLE_TYPES, default='U')
    username = models.CharField(max_length=50, unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='user_set_custom',
        related_query_name='user_custom',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='user_set_custom',
        related_query_name='user_custom',
    )

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_user = User.objects.get(pk=self.pk)
                if old_user.profile_image and old_user.profile_image != self.profile_image:
                    if old_user.profile_image:
                        if os.path.isfile(old_user.profile_image.path):
                            os.remove(old_user.profile_image.path)
            except User.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.profile_image:
            if os.path.isfile(self.profile_image.path):
                os.remove(self.profile_image.path)
        super().delete(*args, **kwargs)


class Auth(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)

    def __str__(self):
        return self.user.fullname

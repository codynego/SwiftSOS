from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    country_code = models.CharField(max_length=4)
    phone_number = models.PositiveIntegerField()
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    medical_history = models.TextField()

    def __str__(self):
        return self.username

class EmergencyContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emergency_contacts')
    relationship = models.CharField(max_length=25)

    def __str__(self):
        return f"Emergency Contact for {self.user.username}"


class EmergencyAlert(models.Model):
    EMERGENCY_TYPES = (
        ('Medical', 'Medical'),
        ('Fire', 'Fire'),
        ('Natural disaster', 'Natural disaster'),
        ('Crime', 'Crime')
    )

    STATUS_TYPE = (
        ('pending', 'pending'),
        ('in progress', 'in progress'),
        ('resolved', 'resolved'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emergencies')
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)
    Emergency_type = models.CharField(max_length=20, choices=EMERGENCY_TYPES)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_TYPE)
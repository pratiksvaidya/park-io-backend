from django.db import models

# Create your models here.
class ParkingSpot(models.Model):
    address = models.CharField(max_length=100)
    rate = models.FloatField()
    contact = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    occupied = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
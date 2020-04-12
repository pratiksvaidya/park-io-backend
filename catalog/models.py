from django.db import models
from mapbox import Geocoder

# Create your models here.
class ParkingSpot(models.Model):
    address = models.CharField(max_length=100)
    rate = models.FloatField()
    contact = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    occupied = models.BooleanField(default=False)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    owner_email = models.CharField(max_length=100)
    reserver_email = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs): 
        try:
            geocoder = Geocoder(access_token="pk.eyJ1IjoicHJhdGlrdmFpZHlhIiwiYSI6ImNrODZ2NzM1MDBpYXAzbm1ydDJyZm00dW0ifQ.B_iyhQhsrVLYbMMxLTNQ8Q").forward(self.address)
            response = geocoder.json()
            location = response['features'][0]
            self.lat = location['center'][0]
            self.lon = location['center'][1]
            self.address = location['place_name']
        except:
            pass

        super(ParkingSpot, self).save(*args, **kwargs) 

    def __str__(self):
        return self.address

    class Meta():
        verbose_name = 'Parking Spot'
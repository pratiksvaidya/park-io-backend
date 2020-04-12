from .models import ParkingSpot
from rest_framework import serializers


class ParkingSpotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = ['address', 'rate', 'contact', 'description', 'occupied', 'email', 'lat', 'lon', 'url']
        read_only = ['lat', 'lon']
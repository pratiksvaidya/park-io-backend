# # from django.shortcuts import render
# from rest_framework.decorators import api_view
# from django.http import HttpResponse

# # Create your views here.

# @api_view(['GET'])
# def public(request):
#     return HttpResponse("You don't need to be authenticated to see this")


from .models import ParkingSpot
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ParkingSpotSerializer


class ParkingSpotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows parking spots to be viewed or edited.
    """
    queryset = ParkingSpot.objects.all().order_by('-created')
    serializer_class = ParkingSpotSerializer
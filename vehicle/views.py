from rest_framework import generics
from vehicle.serializers import VehicleDetailSerializer


class DriverCreateView(generics.CreateAPIView):
    serializer_class = VehicleDetailSerializer

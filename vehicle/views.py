from rest_framework import generics
from vehicle.serializers import DriverDetailSerializer, VehicleDetailSerializer
from vehicle.models import Driver, Vehicle
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class DriversListCreateView(generics.ListCreateAPIView):
    serializer_class = DriverDetailSerializer
    queryset = Driver.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('created_at',)


class DriverDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DriverDetailSerializer
    queryset = Driver.objects.all()


class VehicleListCreateView(generics.ListCreateAPIView):
    serializer_class = VehicleDetailSerializer
    queryset = Vehicle.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('driver_id',)


class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleDetailSerializer
    queryset = Vehicle.objects.all()

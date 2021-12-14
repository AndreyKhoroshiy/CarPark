from rest_framework import generics
from vehicle.serializers import DriverDetailSerializer, VehicleDetailSerializer
from vehicle.models import Driver, Vehicle
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, DateFilter, AllValuesFilter


class DriverFilter(FilterSet):
    created_at__gte = DateFilter(field_name='created_at', lookup_expr='gte')
    created_at__lte = DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Driver
        fields = (
            'created_at__gte',
            'created_at__lte',
        )


class DriversListCreateView(generics.ListCreateAPIView):
    serializer_class = DriverDetailSerializer
    queryset = Driver.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_class = DriverFilter


class DriverDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DriverDetailSerializer
    queryset = Driver.objects.all()


class VehicleFilter(FilterSet):
    with_drivers = AllValuesFilter(field_name='driver_id')

    class Meta:
        model = Vehicle
        fields = (
            'with_drivers',
        )


class VehicleListCreateView(generics.ListCreateAPIView):
    serializer_class = VehicleDetailSerializer
    queryset = Vehicle.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_class = VehicleFilter


class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleDetailSerializer
    queryset = Vehicle.objects.all()

from rest_framework import generics
from vehicle.serializers import DriverDetailSerializer
from vehicle.models import Driver
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




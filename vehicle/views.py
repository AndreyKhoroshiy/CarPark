from rest_framework import generics
from vehicle.serializers import DriverDetailSerializer
from vehicle.models import Driver


class DriversListCreateView(generics.ListCreateAPIView):
    serializer_class = DriverDetailSerializer
    queryset = Driver.objects.all()





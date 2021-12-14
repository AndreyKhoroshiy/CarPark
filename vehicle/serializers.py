from rest_framework import serializers
from vehicle.models import Driver, Vehicle


class DriverDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class VehicleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

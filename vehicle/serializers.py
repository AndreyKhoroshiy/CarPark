from rest_framework import serializers
from vehicle.models import Driver


class VehicleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

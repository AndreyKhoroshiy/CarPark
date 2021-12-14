from django.urls import path
from vehicle.views import DriversListCreateView, DriverDetailView, VehicleListCreateView, VehicleDetailView

urlpatterns = [
    path('drivers/driver/', DriversListCreateView.as_view()),
    path('drivers/driver/<int:pk>/', DriverDetailView.as_view()),
    path('vehicles/vehicle/', VehicleListCreateView.as_view()),
    path('vehicles/vehicle/<int:pk>/', VehicleDetailView.as_view()),
]

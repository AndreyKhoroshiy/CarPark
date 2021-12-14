from django.urls import path
from vehicle.views import DriversListCreateView, DriverDetailView

urlpatterns = [
    path('drivers/driver/', DriversListCreateView.as_view()),
    path('drivers/driver/<int:pk>/', DriverDetailView.as_view()),
]

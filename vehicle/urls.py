from django.urls import path
from vehicle.views import DriverCreateView

urlpatterns = [
    path('drivers/driver/', DriverCreateView.as_view()),

]

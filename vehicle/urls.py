from django.urls import path
from vehicle.views import *

urlpatterns = [
    path('drivers/driver/', DriverCreateView.as_view()),

]

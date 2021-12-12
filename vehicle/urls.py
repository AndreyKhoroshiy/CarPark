from django.urls import path
from vehicle.views import DriversListCreateView

urlpatterns = [
    path('drivers/driver/', DriversListCreateView.as_view()),

]

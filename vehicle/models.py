from django.db import models


class Driver(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Vehicle(models.Model):
    driver_id = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, default=None)
    make = models.CharField(verbose_name='Дата выпуска', max_length=50)
    model = models.CharField(verbose_name='Модель', max_length=50)
    plate_number = models.CharField(verbose_name='Номерной знак', max_length=10)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


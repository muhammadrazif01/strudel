from unicodedata import name
from django.db import models


# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    restaurants = models.Manager()

class Customer(models.Model):
    name = models.CharField(max_length=50)
    reservationC = models.ForeignKey('Reservation', on_delete=models.CASCADE, blank=True, null=True)
    customers = models.Manager()

class Reservation(models.Model):
    customerR = models.ForeignKey(Customer, on_delete=models.CASCADE)
    timeslot = models.CharField(max_length=1)
    status = models.CharField(max_length=30)
    total_seats = models.IntegerField(default=1)
    reservations = models.Manager()
    
class Order(models.Model):
    customerO = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reservationO = models.OneToOneField(Reservation, on_delete=models.CASCADE, primary_key=True)
    orders = models.Manager()





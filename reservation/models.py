from django.db import models
# from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Timeslot(models.Model):
    time_start = models.TimeField()
    time_stop = models.TimeField()
    seat_availability = models.IntegerField()
    is_close = models.BooleanField()
    timeslots = models.Manager()

    def __str__(self):
        return (self.time_start.isoformat() + " - " + self.time_stop.isoformat())

class Schedule(models.Model):
    timeslots = models.ManyToManyField(Timeslot)

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default="Lorem Ipsum")
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True)
    restaurants = models.Manager()

class Fnb(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=30)
    fnbs = models.Manager()

class Order(models.Model):
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    fnb = models.ManyToManyField(Fnb)
    status = models.CharField(default="Pending", max_length=30)
    orders = models.Manager()

class Reservation(models.Model):
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
    timeslot = models.ForeignKey(Timeslot, on_delete=models.CASCADE)
    total_seat = models.IntegerField(default=0)
    status = models.CharField(default="Pending", max_length=30)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    reservations = models.Manager()

class Customer(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    customers = models.Manager()
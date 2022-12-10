from django.contrib import admin
from .models import Reservation, Restaurant, Timeslot, Order, Fnb, Schedule

# Register your models here.
admin.site.register(Reservation)
admin.site.register(Restaurant)
admin.site.register(Timeslot)
admin.site.register(Order)
admin.site.register(Fnb)
admin.site.register(Schedule)

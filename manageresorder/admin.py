from django.contrib import admin
from .models import Reservation, Restaurant, Customer, Order

# Register your models here.
admin.site.register(Reservation)
admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Order)
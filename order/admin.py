from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Order)
admin.site.register(Fnb)
admin.site.register(Menu)
admin.site.register(Reservation)
admin.site.register(Restaurant)
admin.site.register(FnbChoice)
from django.db import models
import datetime

# Timeslot has day properties in it in which that is a member of Schedule models
# When admin would like to create a timeslot, they need to pick a time-slot in which the choices are already pre-defined

DAY_CHOICES = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
]

# Timeslot : day, time start, time stop, total seat, seat availability, dan is close

class Timeslot(models.Model):
    day = models.CharField(max_length=20, choices=DAY_CHOICES, default='SUNDAY')
    time_start = models.TimeField(default=datetime.time(16, 00))
    time_stop = models.TimeField(default=datetime.time(17, 00))
    total_seat = models.IntegerField(default=20)
    seat_availability = models.IntegerField(default=20)
    is_close = models.BooleanField(default=False)
    timeslots = models.Manager()
from django.db import models

DAY_CHOICES = [
    ('MONDAY', 'Monday'),
    ('TUESDAY', 'Tuesday'),
    ('WEDNESDAY', 'Wednesday'),
    ('THURSDAY', 'Thursday'),
    ('FRIDAY', 'Friday'),
    ('SATURDAY', 'Saturday'),
    ('SUNDAY', 'Sunday'),
]

class Schedule(models.Model):
    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    schedules = models.Manager()

    def __str__(self):
         return (self.day)

TIME_SLOT_CHOICES = [
    ('12:00 AM - 01:00 AM', '12:00 AM - 01:00 AM'),
    ('01:00 AM - 02:00 AM', '01:00 AM - 02:00 AM'),
    ('02:00 AM - 03:00 AM', '02:00 AM - 03:00 AM'),
    ('03:00 AM - 04:00 AM', '03:00 AM - 04:00 AM'),
    ('04:00 AM - 05:00 AM', '04:00 AM - 05:00 AM'),
    ('05:00 AM - 06:00 AM', '05:00 AM - 06:00 AM'),
    ('06:00 AM - 07:00 AM', '06:00 AM - 07:00 AM'),
    ('07:00 AM - 08:00 AM', '07:00 AM - 08:00 AM'),
    ('08:00 AM - 09:00 AM', '08:00 AM - 09:00 AM'),
    ('09:00 AM - 10:00 AM', '09:00 AM - 10:00 AM'),
    ('10:00 AM - 11:00 AM', '10:00 AM - 11:00 AM'),
    ('11:00 AM - 12:00 AM', '11:00 AM - 12:00 AM'),
    ('12:00 PM - 01:00 PM', '12:00 PM - 01:00 PM'),
    ('01:00 PM - 02:00 PM', '01:00 PM - 02:00 PM'),
    ('02:00 PM - 03:00 PM', '02:00 PM - 03:00 PM'),
    ('03:00 PM - 04:00 PM', '03:00 PM - 04:00 PM'),
    ('04:00 PM - 05:00 PM', '04:00 PM - 05:00 PM'),
    ('05:00 PM - 06:00 PM', '05:00 PM - 06:00 PM'),
    ('06:00 PM - 07:00 PM', '06:00 PM - 07:00 PM'),
    ('07:00 PM - 08:00 PM', '07:00 PM - 08:00 PM'),
    ('08:00 PM - 09:00 PM', '08:00 PM - 09:00 PM'),
    ('09:00 PM - 10:00 PM', '09:00 PM - 10:00 PM'),
    ('10:00 PM - 11:00 PM', '10:00 PM - 11:00 PM'),
    ('11:00 PM - 12:00 PM', '11:00 PM - 12:00 PM'),
]

class Timeslot(models.Model):
    day = models.ManyToManyField(Schedule)
    time_range = models.CharField(max_length=100, choices=TIME_SLOT_CHOICES)
    total_seat = models.IntegerField()
    seat_availability = models.IntegerField()
    is_close = models.BooleanField()
    timeslots = models.Manager()
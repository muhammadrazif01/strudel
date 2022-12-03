from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Schedule(models.Model):
    identifier = models.IntegerField(validators=[
            MaxValueValidator(7),
            MinValueValidator(0)
        ])
    day = models.CharField(max_length=30)
    
    def __str__(self):
        return "%s %s" % (self.identifier, self.day)

class Timeslot(models.Model):
    day_id = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    identifier = models.IntegerField(validators=[
            MaxValueValidator(24),
            MinValueValidator(1)
        ])
    time_range = models.TimeField()
    total_seat = models.PositiveIntegerField()
    seat_availability = models.PositiveIntegerField()
    is_close = models.BooleanField()

    def __str__(self):
        return "%s %s %s %s %s %s" % (self.day_id, self.identifier, self.time_range, self.total_seat, self.seat_availability, self.is_close)

    class Meta:
        ordering = ['id']
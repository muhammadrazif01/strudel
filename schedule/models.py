from django.db import models

days = (
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'))

class Schedule(models.Model):
    day = models.CharField(max_length=100, choices=days, default='Sunday')

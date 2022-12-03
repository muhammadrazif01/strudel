from django import forms

from .models import Schedule, Timeslot

class ScheduleForm(forms.ModelForm):
   class Meta:
     model = Schedule
     fields = '__all__'

class TimeslotForm(forms.ModelForm):
   class Meta:
     model = Timeslot
     fields = '__all__'
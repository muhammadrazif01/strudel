from django.forms import Form
from django import forms
from .models import Timeslot, Restaurant



class CreateReservationForm(forms.Form):
    restaurant_name = forms.CharField()

    # timestart_choice = Timeslot.timeslots.filter(restaurant_set=restaurant_id, is_close=False).values_list('time_start', flat=True).order_by('time_start')
    # timestop_choice = Timeslot.timeslots.filter(restaurant_set=restaurant_id, is_close=False).values_list('time_stop', flat=True).order_by('time_start')

    # timeslot_choice = []

    # for timestart, timestop in zip(timestart_choice, timestop_choice):
    #     timeslot_choice.append(timestart.isoformat() + "-" + timestop.isoformat())

    timeslot_id = forms.ChoiceField()
    total_seat = forms.IntegerField()

    def __init__(self, restaurant_id):
        super(CreateReservationForm, self).__init__()
        restaurant = Restaurant.restaurants.get(id=restaurant_id)
        self.fields['restaurant_name'] = forms.CharField(max_length=5, label='Restaurant Name', widget=forms.TextInput(attrs={'readonly':'readonly'}), initial=restaurant.name)
        
        timeslot = restaurant.schedule.timeslots.filter(is_close=False)
        CHOICES = tuple((m.id, m) for m in timeslot)
        self.fields['timeslot_id'] = forms.ChoiceField(choices=CHOICES, label='Timeslot')
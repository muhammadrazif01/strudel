from django import forms

class CreateTimeslotForm(forms.Form):
  day = forms.ChoiceField()
  time_start = forms.TimeField()
  time_stop = forms.TimeField()
  total_seat = forms.IntegerField()
  seat_availability = forms.IntegerField()

  def __init__(self):
      super(CreateTimeslotForm, self).__init__()
    
      DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
      ]

      self.fields['day'] = forms.ChoiceField(choices=DAY_CHOICES, label='Day')
      self.fields['time_start'] = forms.TimeField(label='Time Start', widget=forms.TimeInput(attrs={'type': 'time'}))
      self.fields['time_stop'] = forms.TimeField(label='Time Stop', widget=forms.TimeInput(attrs={'type': 'time'}))
      self.fields['total_seat'] = forms.IntegerField(label='Total Seat', widget=forms.NumberInput())
      self.fields['seat_availability'] = forms.IntegerField(label='Seat Availability', widget=forms.NumberInput())

class UpdateTimeslotForm(forms.Form):
  id = forms.ImageField()
  total_seat = forms.IntegerField()

  def __init__(self):
      super(UpdateTimeslotForm, self).__init__()
      self.fields['id'] = forms.ChoiceField(label='ID', widget=forms.NumberInput())
      self.fields['total_seat'] = forms.IntegerField(label='Total Seat', widget=forms.NumberInput())
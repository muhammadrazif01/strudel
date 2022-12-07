from django.shortcuts import render

from .models import Timeslot
from .forms import CreateTimeslotForm

def mainpage(request):
    response = {}
    return render(request, 'mainpage.html', response)

def create_timeslot(request):
    if request.method == 'POST':
        day = request.POST['day']
        time_start = request.POST['time_start']
        time_stop = request.POST['time_stop']
        total_seat = request.POST['total_seat']
        seat_availability = request.POST['seat_availability']
    form = CreateTimeslotForm()    
    data = {
        'form': form,   
    }
    return render(request, "create_timeslot.html", data)
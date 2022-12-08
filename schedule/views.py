from django.shortcuts import render, redirect
from django.contrib import messages

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
        ts = Timeslot.timeslots.create(
            day=day,
            time_start=time_start,
            time_stop=time_stop,
            total_seat=total_seat,
            seat_availability=seat_availability,
            is_close=False)
        ts.save()
        print(ts.id)
        return redirect('/schedule/show-timeslot')
    form = CreateTimeslotForm()    
    data = {
        'form': form,   
    }
    return render(request, "create_timeslot.html", data)

def show_timeslot(request):
    timeslot = Timeslot.timeslots.all()
    data = {
        'list_timeslot': timeslot,
    }
    return render(request, "show_timeslot.html", data) 

def delete_timeslot(request, id):
    query = Timeslot.timeslots.get(id=id)
    total_seat = query.total_seat
    seat_availability = query.seat_availability
    if (total_seat == seat_availability):
        query.delete()
        return redirect('/schedule/show-timeslot')
    else:
        return redirect('/schedule')
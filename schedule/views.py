from django.shortcuts import render, redirect

from .models import Timeslot
from .forms import CreateTimeslotForm, UpdateTimeslotForm

def create_timeslot(request):
    if request.method == 'POST':
        day = request.POST['day']
        time_start = request.POST['time_start']
        time_stop = request.POST['time_stop']
        total_seat = request.POST['total_seat']
        seat_availability = request.POST['seat_availability']
        hour_start = int((str(time_start)[0:1]))
        hour_stop = int((str(time_stop)[0:1]))
        minute_start = int((str(time_start)[3:4]))
        minute_stop = int((str(time_stop)[3:4]))
        if ((int(seat_availability) >= 0) and (int(total_seat) >= 0)): 
            if (int(seat_availability) <= int(total_seat)):
                if ((hour_start < hour_stop) or (hour_start == hour_stop and minute_stop > minute_start)):
                    ts = Timeslot.timeslots.create(
                        day=day,
                        time_start=time_start,
                        time_stop=time_stop,
                        total_seat=total_seat,
                        seat_availability=seat_availability,
                        is_close=False)
                    ts.save()
                    return redirect('/schedule')
                else:
                    return redirect('/schedule/warning')
            else:
                return redirect('/schedule/warning')
        else:
                return redirect('/schedule/warning')
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
        return redirect('/schedule')
    elif (seat_availability == 0):
        query.delete()
        return redirect('/schedule')
    else:
        return redirect('/schedule/warning')

def update_timeslot(request):
    if request.method == 'POST':
        id = request.POST['id']
        total_seat = request.POST['total_seat']
        is_close = request.POST['is_close']
        if (int(total_seat) >= 1):
            if (is_close == 'Yes'):
                ts = Timeslot.timeslots.get(id=id)
                ts.seat_availability = 0
                ts.save()
            else:
                ts = Timeslot.timeslots.get(id=id)
                total_before_update = ts.total_seat
                availability_before_update = ts.seat_availability
                gap = total_before_update - availability_before_update
                ts.seat_availability = int(total_seat) - int(gap)
                ts.total_seat = int(total_seat)
                ts.save()
            return redirect('/schedule')
        else:
            return redirect('/schedule/warning')
    form = UpdateTimeslotForm()    
    data = {
        'form': form,   
    }
    return render(request, "update_timeslot.html", data)

def reserve_timeslot(request, id):
    query = Timeslot.timeslots.get(id=id)
    seat_availability = query.seat_availability
    if (int(seat_availability) != 0):
        query.seat_availability = int(seat_availability) - 1;
        query.save()
        return redirect('/schedule')
    else:
        return redirect('/schedule/warning')

def cancel_reservation(request, id):
    query = Timeslot.timeslots.get(id=id)
    total_seat = query.total_seat
    seat_availability = query.seat_availability
    if (int(seat_availability) != int(total_seat)):
        query.seat_availability = int(seat_availability) + 1;
        query.save()
        return redirect('/schedule')
    else:
        return redirect('/schedule/warning')

def start_over(request):
    Timeslot.timeslots.all().delete()
    return redirect('/schedule')

def warning(request):
    response = {}
    return render(request, 'warning.html', response)
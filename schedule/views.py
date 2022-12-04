from sqlite3 import Time
from .models import Schedule, Timeslot
from .forms import ScheduleForm, TimeslotForm

from django.template.response import TemplateResponse
from django.shortcuts import render
from django.http import response
from django.http.response import HttpResponseRedirect

def mainpage(request):
    response = {}
    return render(request, 'mainpage.html', response)

def add_schedule(request):
   form = ScheduleForm()
   return render(request,
            'add_schedule_form.html',
            {'form': form})

def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save()
            return render(request, 'mainpage.html', {})
    else:
        form = ScheduleForm()
    return render(request,
                'add_schedule_form.html',
                {'form': form})

def add_timeslot(request):
   form = TimeslotForm()
   return render(request,
            'add_timeslot_form.html',
            {'form': form})

def add_timeslot(request):
    if request.method == 'POST':
        form = TimeslotForm(request.POST)
        if form.is_valid():
            timeslot = form.save()
            return render(request, 'mainpage.html', {})
    else:
        form = TimeslotForm()
    return render(request,
                'add_timeslot_form.html',
                {'form': form})

def timeslot_list(request):
    allschedules = Schedule.schedules.all()
    alltimeslots = Timeslot.timeslots.all()
    response = {'alltimeslots' : alltimeslots, 'allschedules' : allschedules}
    return render(request, 'all_timeslot.html', response)

def update_schedule(request):
    response = {}
    return render(request, 'update_schedule_form.html', response)

def delete_schedule(request):
    response = {}
    return render(request, 'delete_schedule_form.html', response)

def add_schedule_monday(request):
    response = {}
    return render(request, 'schedulemonday.html', response)

def add_schedule_tuesday(request):
    response = {}
    return render(request, 'scheduletuesday.html', response)

def add_schedule_wednesday(request):
    response = {}
    return render(request, 'schedulewednesday.html', response)

def add_schedule_thursday(request):
    response = {}
    return render(request, 'schedulethursday.html', response)

def add_schedule_friday(request):
    response = {}
    return render(request, 'schedulefriday.html', response)

def add_schedule_saturday(request):
    response = {}
    return render(request, 'schedulesaturday.html', response)

def add_schedule_sunday(request):
    response = {}
    return render(request, 'schedulesunday.html', response)
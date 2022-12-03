from django.shortcuts import render
from django.http import response
from django.http.response import HttpResponseRedirect
from .forms import ScheduleForm
from .models import Schedule

def mainpage(request):
    response = {}
    return render(request, 'mainpage.html', response)

def add_schedule(request):
    context = {}
    form = ScheduleForm(request.POST or None)
    if (request.method == 'POST' and form.is_valid()):
        cd = form.cleaned_data
        schedule = Schedule(day=cd['day'])
        schedule.save() 
        return HttpResponseRedirect('/manageschedule')
    context['form'] = form
    return render(request, 'add_schedule_form.html', context)

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
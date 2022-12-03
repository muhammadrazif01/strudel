from django.urls import path
from .views import mainpage, add_schedule, update_schedule, delete_schedule, add_timeslot, timeslot_list
from .views import add_schedule_monday, add_schedule_tuesday, add_schedule_wednesday
from .views import add_schedule_thursday, add_schedule_friday, add_schedule_saturday, add_schedule_sunday

urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('add-schedule', add_schedule, name='add_schedule'),
    path('add-timeslot', add_timeslot, name='add_timeslot'),
    path('all-timeslot', timeslot_list, name='timeslot_list'),
    path('update-schedule', update_schedule, name='update_schedule'),
    path('delete-schedule', delete_schedule, name='delete_schedule'),
    path('add-schedule-monday', add_schedule_monday, name='add_schedule_monday'),
    path('add-schedule-tuesday', add_schedule_tuesday, name='add_schedule_tuesday'),
    path('add-schedule-wednesday', add_schedule_wednesday, name='add_schedule_wednesday'),
    path('add-schedule-thursday', add_schedule_thursday, name='add_schedule_thursday'),
    path('add-schedule-friday', add_schedule_friday, name='add_schedule_friday'),
    path('add-schedule-saturday', add_schedule_saturday, name='add_schedule_saturday'),
    path('add-schedule-sunday', add_schedule_sunday, name='add_schedule_sunday'),
]

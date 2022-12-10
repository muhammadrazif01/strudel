from django.urls import path
from .views import create_timeslot, show_timeslot, delete_timeslot, update_timeslot, reserve_timeslot, cancel_reservation, start_over, warning

urlpatterns = [
    path('', show_timeslot, name='show_timeslot'),
    path('create-timeslot', create_timeslot, name='create_timeslot'),
    path('delete-timeslot/<int:id>', delete_timeslot, name='delete_timeslot'),
    path('update-timeslot', update_timeslot, name='update_timeslot'),
    path('reserve-timeslot/<int:id>', reserve_timeslot, name='reserve_timeslot'),
    path('cancel-reservation/<int:id>', cancel_reservation, name='cancel_reservation'),
    path('start-over', start_over, name='start_over'),
    path('warning', warning, name='warning')
]

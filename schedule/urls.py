from django.urls import path
from .views import create_timeslot, show_timeslot, delete_timeslot, update_timeslot, warning

urlpatterns = [
    path('', show_timeslot, name='show_timeslot'),
    path('create-timeslot', create_timeslot, name='create_timeslot'),
    path('delete-timeslot/<int:id>', delete_timeslot, name='delete_timeslot'),
    path('update-timeslot', update_timeslot, name='update_timeslot'),
    path('warning', warning, name='warning')
]

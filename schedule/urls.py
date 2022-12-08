from django.urls import path
from .views import mainpage, create_timeslot, show_timeslot, delete_timeslot

urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('create-timeslot', create_timeslot, name='create_timeslot'),
    path('show-timeslot', show_timeslot, name='show_timeslot'),
    path('delete-timeslot/<int:id>', delete_timeslot, name='delete_timeslot'),
]

from django.urls import path
from .views import mainpage, create_timeslot

urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('create-timeslot', create_timeslot, name='create_timeslot')
]

from django.shortcuts import render, redirect
from .models import Reservation, Restaurant, Customer, Order
# Create your views here.

def reservation_index(request):
    # Need to change it for specified restaurant admins
    pending = Reservation.reservations.filter(status='Pending')
    active = Reservation.reservations.filter(status='Active')
    cancelled = Reservation.reservations.filter(status='Cancelled')

    response = {
        'pending_reservations' : pending,
        'active_reservations' : active,
        'cancelled_reservations' : cancelled
    }

    return render(request, "read_reservations.html", response)

def read_reservation_detail(request, id_res):
    reservation = Reservation.reservations.filter(id=id_res)
    
    response = {
        "reservation" : reservation,
    }

    return render(request, "read_reservation_detail.html", response)

def accept_reservation(request, id_res):
    reservation = Reservation.reservations.get(id=id_res)

    reservation.status = 'Active'
    reservation.save()

    return redirect('manageresorder:index')

def reject_reservation(request, id_res):
    reservation = Reservation.reservations.get(id=id_res)

    reservation.status = 'Cancelled'
    reservation.save()

    return redirect('manageresorder:index')


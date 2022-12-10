from django.shortcuts import render, redirect
from .models import Reservation as ReservationModel, Restaurant as RestaurantModel, Timeslot as TimeslotModel, Order as OrderModel
from .forms import CreateReservationForm

# Create your views here.
def home_index(request):
    return render(request, 'home_index.html')

def create_reservation(request, id):
    message =""
    restaurant_id = id
    # restaurant = RestaurantModel.restaurants.get(id=restaurant_id)
    # timeslots = restaurant.timeslots
    if request.method == 'POST':
        timeslot_id = request.POST['timeslot_id']
        timeslot = TimeslotModel.timeslots.get(id=timeslot_id)
        total_seat = request.POST['total_seat']
        try:
            if (timeslot.seat_availability >= int(total_seat)):
                obj = ReservationModel.reservations.create(restaurant_id=restaurant_id, total_seat=total_seat, timeslot=timeslot)
                obj.save()
                return redirect('/my-reservation/')
            else:
                message = "Kapasitas kursi tidak memadai. Reservasi tidak berhasil dibuat."
        except Exception as e:
            print(e)
            message = "Reservasi tidak berhasil dibuat."

    form = CreateReservationForm(restaurant_id=restaurant_id)
    
    data = {
        'form': form,
        'message': message,
        'restaurant_id': restaurant_id,   
    }

    return render(request, "create_reservation.html", data)

def read_reservation(request):
    reservation = ReservationModel.reservations.all()

    data = {
        'list_reservation': reservation,
    }

    return render(request, "read_reservation.html", data) 

def reservation_detail(request, id):
    reservation = ReservationModel.reservations.get(id=id)

    if (reservation.status == 'Pending' or reservation.status == 'Confirmed'):
        status = True
    else:
        status = False
    
    if (reservation.order is not None):
        order = True
    else:
        order = False

    data = {
        'reservation': reservation,
        'status': status,
        'order': order,
    }

    return render(request, "reservation_detail.html", data) 

def cancel_reservation(request, id):
    reservation = ReservationModel.reservations.get(id=id)

    if (reservation.status == 'Pending'):
        reservation.status = 'Canceled'
        reservation.save()
    elif (reservation.status == 'Confirmed'):
        reservation.status = 'Waiting for cancelation confirmation'
        reservation.save()

    return redirect('/my-reservation/')

def read_restaurant(request):
    restaurants = RestaurantModel.restaurants.all()

    data = {
        'list_restaurant': restaurants,
    }

    return render(request, "read_restaurant.html", data)

def restaurant_detail(request, id):
    restaurant = RestaurantModel.restaurants.get(id=id)

    schedule = restaurant.schedule.timeslots.filter(is_close=False)

    data = {
        'restaurant': restaurant,
        'schedule': schedule,
    }

    return render(request, "restaurant_detail.html", data) 

def read_order(request, id):
    order = OrderModel.orders.get(id=id)

    fnbs = order.fnb.all()

    data = {
        'order': order,
        'fnbs': fnbs,
    }

    return render(request, "read_order.html", data)

def cancel_order(request, id):
    order = OrderModel.orders.get(id=id)

    if (order.status == 'Pending'):
        order.status = 'Canceled'
        order.save()

    return redirect('/my-reservation/')
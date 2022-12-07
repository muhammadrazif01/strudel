from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def order_index(request):
    response = {
        "orders": Order.orders.order_by('-id') # should return orders made by customer that is already logged in now only
    }
    return render(request, "order_index.html", response)

def show_menu(request):
    reservation_id = request.POST['reservation_id']
    reservation = Reservation.reservations.get(id=reservation_id)
    restaurant = Restaurant.restaurants.get(id=reservation.restaurant.id)
    menu = Menu.menus.get(restaurant=restaurant)
    response = {
        "menu" : menu,
        "menus": menu.fnb.all(),
        'reservation_id' : reservation_id
    }
    return render(request, "show_menu.html", response)

def order_detail(request, order_id):
    order = Order.orders.get(id=order_id)
    response = {
        "id": order.id,
        "restaurant": order.reservation.restaurant,
        "fnbchoices": order.fnbchoice_set.all(),
        "total_price": order.total_price,
        "status" : order.status,
        "payment_method": order.payment_method
    }
    return render(request, "order_detail.html", response)

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        try:
            choices = json.loads(request.body.decode("utf-8"))
            reservation_id = choices.pop('reservation_id')
            new_order = Order.orders.create(reservation_id=reservation_id, total_price=0, payment_method='-', status='Waiting for payment')
            new_order.save()
            for i in choices.keys():
                picked_fnb = Fnb.fnbs.get(id=i)
                new_choice = FnbChoice.fnbchoices.create(order=new_order, fnb=picked_fnb, amount=int(choices[i]))
                new_choice.save()

                new_order.total_price += new_choice.total_price()
                new_order.save()
            return HttpResponse(new_order.id)
        except:
            return HttpResponse(None)
    return HttpResponse(None)

@csrf_exempt
def pay_order(request, order_id):
    response = {}
    order = Order.orders.get(id=order_id)
    if request.method == 'POST':
        try:
            payment_method = json.loads(request.body.decode("utf-8"))['payment_method']
            order = Order.orders.get(id=order_id)
            order.payment_method = payment_method
            order.status = "Waiting for restaurant's confirmation"
            order.save()
            return HttpResponse(order_id)
        except:
            return HttpResponse(None)
    response = {
        "total": order.total_price,
        "order_id": order_id,
        "payment_method": ["GoPay", "OVO", "DANA", "Credit/Debit Card", "Bank Transfer", "QRIS"]
    }
    return render(request, "pay_order.html", response)

@csrf_exempt
def cancel_order(request, order_id):
    if request.method == 'POST':
        try:
            order = Order.orders.get(id=order_id)
            if order.status == "Waiting for restaurant's confirmation" :
                order.status = "Cancelled"
                order.save()
            else :
                order.status = "Cancellation requested"
                order.save()
            return HttpResponse(order_id)
        except:
            return HttpResponse(None)
    return HttpResponse(None)
            

def show_restaurants(request):
    response = {
        "restaurants" : Restaurant.restaurants.all()
    }
    return render(request, "show_restaurants.html", response)

def show_reservations(request):
    response = {
        "reservations" : Reservation.reservations.all()
    }
    return render(request, "show_reservations.html", response)
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def order_index(request):
    response = {
        "orders": Order.orders.all() # should return orders made by customer that is already logged in now only
    }
    print(len(response['orders']))
    return render(request, "order_index.html", response)

def show_menu(request):
    menu = Menu.menus.get(restaurant_id=request.POST['restaurant_id']) # get menu by restaurant id
    response = {
        "menu" : menu,
        "menus": menu.fnb.all()
    }
    return render(request, "show_menu.html", response)

def order_detail(request):
    order = Order.orders.get(id=request.POST['order_id']) # bener gak sih ? 
    response = {
        "restaurant": order.restaurant,
        "fnbchoices": order.fnbchoice_set.objects.all(),
        "total_price": order.total_price,
        "status" : order.status,
        "payment_method": order.payment_method
    }
    return render(request, "order_detail.html", response)

@csrf_exempt
def order_summary(request):
    response = {}
    print(request)
    if request.is_ajax():
        if request.method == 'POST':
            print(request.body)
    return render(request, "order_summary.html", response)

def pay_order(request, order_id): # should throw order id
    # order = Order.orders.get(id=order_id) # bener gak sih ?
    response = {
        "total": 2000, # should get from order gotten above
        "payment_method": ["GoPay", "OVO", "DANA", "Credit/Debit Card", "Bank Transfer", "QRIS"]
    }
    return render(request, "pay_order.html", response)

def show_restaurants(request):
    response = {
        "restaurants" : Restaurant.restaurants.all()
    }
    return render(request, "show_restaurants.html", response)
from django.urls import path
from .views import *

app_name = 'order'

urlpatterns = [
    path('order/', order_index, name="index"),
    path('order/detail/<int:order_id>', order_detail, name="detail"),
    path('order/menu', show_menu, name="show_menu"),
    path('order/create', create_order, name="create_order"),
    path('order/pay/<int:order_id>', pay_order, name="pay_order"),
    path('order/cancel/<int:order_id>', cancel_order, name="cancel_order"),
    path('order/restaurants', show_restaurants, name="show_restaurants"),
    path('order/reservations', show_reservations, name="show_reservations"),
]
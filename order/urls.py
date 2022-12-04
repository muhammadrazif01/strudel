from django.urls import path
from .views import *

app_name = 'order'

urlpatterns = [
    path('order/', order_index, name="index"),
    path('order/detail', order_detail, name="detail"),
    path('order/menu', show_menu, name="show_menu"), # throw restaurant id
    path('order/summary', order_summary, name="show_summary"),
    path('order/pay/<int:order_id>', pay_order, name="pay_order"),
    path('order/restaurants', show_restaurants, name="show_restaurants"),
]
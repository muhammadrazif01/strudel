from django.urls import path
from .views import home_index, create_reservation, read_reservation, reservation_detail, cancel_reservation, read_order, read_restaurant, restaurant_detail

app_name = "reservation"

urlpatterns = [
    path('home/', home_index, name='home_index'),
    path('reservation/create/<int:id>', create_reservation, name='create_reservation'),
    path('my-reservation/', read_reservation, name='read_reservation'),
    path('my-reservation/<int:id>', reservation_detail, name='reservation_detail'),
    path('my-reservation/cancel/<int:id>', cancel_reservation, name='cancel_reservation'),
    path('my-reservation/my-order/<int:id>', read_order, name='read_order'),
    path('restaurants/', read_restaurant, name='read_restaurant'),
    path('restaurants/<int:id>', restaurant_detail, name='restaurant_detail'),
]
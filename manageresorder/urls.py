from django.urls import path
from . import views

app_name = 'manageresorder'

urlpatterns = [
    path('reservations', views.reservation_index, name='index'),
    path('res_detail/<str:id_res>/', views.read_reservation_detail, name ='res_detail'),
    path('reservations/cancellation/<str:id_res>', views.reject_reservation, name='reject'),
    path('reservations/activation/<str:id_res>', views.accept_reservation, name='accept')
]
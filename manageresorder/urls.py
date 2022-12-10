from django.urls import path
from . import views

app_name = 'manageresorder'

urlpatterns = [
    path('manageres', views.reservation_index, name='index'),
    path('manageres/<str:id_res>/', views.read_reservation_detail, name ='res_detail'),
    path('manageres/cancellation/<str:id_res>', views.reject_reservation, name='reject'),
    path('manageres/activation/<str:id_res>', views.accept_reservation, name='accept')
]
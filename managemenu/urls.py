from django.urls import path
from .views import *

app_name = 'managemenu'
urlpatterns = [
    path('managemenu/', index),
    path('managemenu/create', create),
    path('managemenu/edit/<int:id>', edit),
    path('managemenu/update/<int:id>', update),
    path('managemenu/delete/<int:id>', delete),
]